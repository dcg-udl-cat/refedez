{inputs, ...}: {
  imports = [inputs.treefmt-nix.flakeModule inputs.pre-commit-hooks.flakeModule];
  perSystem = {
    pkgs,
    lib,
    ...
  }: let
    python = (import ./venv.nix) {inherit inputs pkgs lib;};
    venv = python.pythonSet.mkVirtualEnv "refedez_venv" python.workspace.deps.all;
    refedezPkg = pkgs.writeShellScriptBin "refedez" ''
      exec -a refedez ${venv}/bin/refedez "$@"
    '';
    pytest = pkgs.stdenv.mkDerivation {
      name = "refedez-pytest";
      src = ../.;
      nativeBuildInputs = [
        venv
      ];
      dontConfigure = true;
      # Because this package is running tests, and not actually building the main package
      # the build phase is running the tests.
      #
      # In this particular example we also output a HTML coverage report, which is used as the build output.
      buildPhase = ''
        runHook preBuild
        pytest
        runHook postBuild
      '';
      installPhase = ''
        mkdir -p $out
        # publish the coverage report to $out
        if [ -d htmlcov ]; then
          cp -r htmlcov $out/
        fi
        # at minimum, leave a success marker
        echo "pytest passed on $(date -u)" > $out/ok
      '';
    };
  in {
    packages = rec {
      refedez = refedezPkg;
      refedez-wheel = python.pythonSet.refedez.override {
        pyprojectHook = python.pythonSet.pyprojectDistHook;
      };
      default = refedez-wheel;
    };
    apps.refedez = {
      type = "app";
      program = refedezPkg;
      meta.description = "ReFedEz: A python library for making federated learning easy and reproducible";
    };
    checks = {
      inherit pytest;
    };
  };
}

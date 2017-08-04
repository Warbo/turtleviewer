{ pkgs ? import <nixpkgs> {} }:

# TODO: Use python.withPackages to get pygame, etc.
with pkgs;
stdenv.mkDerivation {
  name         = "TurtleConvert";
  buildInputs  = [ makeWrapper ];
  src          = ./TurtleConvert.py;
  unpackPhase  = "true";
  installPhase = ''
    mkdir -p "$out/bin"
    makeWrapper "$src" "$out/bin/TurtleConvert" --prefix PATH : "${python}/bin"
  '';
}

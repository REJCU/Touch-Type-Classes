{
  description = "Modern Python 3.14 Development Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      # Set your system architecture here
      system = "x86_64-linux"; 
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          # The latest stable interpreter
          python314
          
          # Modern tooling
          uv           # Faster alternative to pip/venv
          ruff         # Fast linter and formatter
          pyright      # Static type checker
        ];

        shellHook = ''
          echo "✨ Python 3.14 Dev Shell Active"
          echo "System: ${system}"
          python --version
          
          # Optional: Create a local .venv if it doesn't exist
          if [ ! -d ".venv" ]; then
            uv venv
          fi
          source .venv/bin/activate
        '';
      };
    };
}

import argparse
import subprocess
import sys


HF_REPO = "llm-jp/llm-jp-moshi-v1"


def main():
    parser = argparse.ArgumentParser(
        description="Launch LLM-jp-Moshi-v1 web server"
    )
    parser.add_argument(
        "--hf-repo",
        default=HF_REPO,
        help=f"HuggingFace Hub repository (default: {HF_REPO})",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8998,
        help="Port to listen on (default: 8998)",
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to bind to (default: localhost)",
    )
    args, extra = parser.parse_known_args()

    cmd = [
        sys.executable, "-m", "moshi.server",
        "--hf-repo", args.hf_repo,
        "--port", str(args.port),
        "--host", args.host,
        *extra,
    ]
    print(f"Starting server: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

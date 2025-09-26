import os
import sys
import google.generativeai as genai
import absl.logging

# stderr 임시 리다이렉트
class SuppressStderr:
    def __enter__(self):
        import os
        self.null_fd = os.open(os.devnull, os.O_RDWR)
        self.old_stderr_fd = os.dup(2)
        os.dup2(self.null_fd, 2)
    def __exit__(self, exc_type, exc_val, exc_tb):
        import os
        os.dup2(self.old_stderr_fd, 2)
        os.close(self.null_fd)
        os.close(self.old_stderr_fd)

def request(question):
    os.environ["GRPC_VERBOSITY"] = "ERROR"
    os.environ["GRPC_CPP_MIN_LOG_LEVEL"] = "3"
    absl.logging.set_verbosity('error')

    with SuppressStderr():
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY 환경 변수가 설정되어 있지 않습니다.")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(question)
    return response.text
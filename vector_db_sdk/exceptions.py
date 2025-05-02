class APIError(Exception):
    def __init__(self, status_code: int, detail: any):
        self.status_code = status_code
        self.detail = detail
        message = f"API error (status {status_code}): {detail}"
        if status_code == 422 and isinstance(detail, list):
            errors = [f"{err['loc']}: {err['msg']}" for err in detail]
            message += "\nDetails:\n" + "\n".join(errors)
        super().__init__(message)
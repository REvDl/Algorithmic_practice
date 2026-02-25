from collections import Counter

ALLOWED_PREFIX = ["[INFO]", "[ERROR]", "[DEBUG]"]  # в дальнейшем

logg = [
	"[INFO] Server started",
	"[ERROR] Database connection failed",
	"[DEBUG] Checking cache",
	"[INFO] Request received",
	"[ERROR] Timeout on port 80",
	"[INFO] Process finished"
]


def count_logs(file_name:str):
    with open(file_name, "r", encoding="utf-8") as f:
        def get_prefix(line: str):
            return line.split()[0]


        counts = dict(Counter(
            prefix for log in f
            if (prefix := get_prefix(log)).startswith("[")
            and prefix.endswith("]")
            and prefix in ALLOWED_PREFIX
        ))
        f.seek(0)
        for i in f:
            if get_prefix(i) == "[ERROR]":
                print(i.replace("[ERROR]", "").strip())
        return counts


print(count_logs("loggs_file.txt"))

from task_domain_008.core import Record, stable_summary

if __name__ == "__main__":
    print(stable_summary(Record("demo", "v1", "draft", "operator")))

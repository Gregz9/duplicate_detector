test_path1 = "~/Programs/test_dir/d/a.txt"

assert "/d/" in test_path1

if "test_dir/" in test_path1:
    print("Success")

# Why ["1.png", "10.png", "2.png"] is sorted?
- This Docker Image changes file names like "00001.png" if their type is in ["jpg", "png", "webp", "gif", "jpeg", "jfif"]
- You must set volume destination as "/target" in the container.
- Every changed log will be printed.
- It is made for The Synology system. so It ignores "@eaDir" Directory.
- Thanks.

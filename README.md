# Why ["1.png", "10.png", "2.png"] is sorted?
- This Docker Image changes file names like "00001.png" if their type is png, jpg, webp.
- You must set volume destination as "/target" in the container.
- It is made for The Synology system. so It ignores "@eaDir" Directory.
- Every changed log will be printed.
- Thanks


### How
 - install dependencies `pip install -r requirements.txt`
 - run `pyro4-ns -n localhost -p 7777`
 - server `cd server && python greet_server.py`
 - client `cd client && python client.py`

### Available Commands
- `ls` : get all files in server storage directory  \
  option : `-a` / `-all`\
  example : `ls -a`
- `mk` : make new file/files  
  syntax : `mk file1 file2 file3`  \
  example : `mk text.txt "lorem ipsum.py"`
- `rm` : delete file/files  
  syntax : `rm file1 file2 file3`  \
  example : `rm text.txt "lorem ipsum.py"`
- `cat` : read file  
  syntax : `cat file`  \
  example : `cat text.txt`
- `update` : update file or create new file if not exists  
  option : `--append` / `-a`, `--overwrite` / `-o`\
  syntax : `update option file content`  \
  example : `update --append text.txt "lorem ipsumsit dolor amet"`
- `exit` : exit  
  syntax : `exit`  \
  example : `exit`
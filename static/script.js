upForm.onsubmit=async(e)=>{
  e.preventDefault();
  const file=document.getElementById('file').files[0];
  if(!file)return;
  const xhr=new XMLHttpRequest();
  xhr.upload.onprogress=(ev)=>{
    document.getElementById('progress').style.width=(ev.loaded/ev.total*100)+'%';
  };
  xhr.onload=()=>{
    if(xhr.status===200){location.reload();}
  };
  xhr.open('POST','/upload');
  const fd=new FormData();
  fd.append('file',file);
  xhr.send(fd);
};
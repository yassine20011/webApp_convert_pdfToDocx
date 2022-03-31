const input = document.getElementById("id_file");
const text = document.getElementById("span");
const btn = document.getElementById("upload-btn");

input.addEventListener("change", () => {
    const path = input.value.split('\\');
    const filename = path[path.length - 1];

    text.innerText = filename ? filename : "Choose file";
   if(filename)
    btn.classList.add("chosen")
   else
    btn.classList.remove("chosen")
})




var r = document.getElementById("id_file");
r.className += "form-control";

input.setAttribute('aria-describedby', 'button-addon2');
input.setAttribute("required", "") 
const input = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const result = document.getElementById("result");

input.onchange = async () => {
	const file = input.files[0];
	preview.src = URL.createObjectURL(file);
	preview.style.display = "block";

	const formData = new FormData();
	formData.append("file", file);

	const res = await fetch("http://127.0.0.1:8000/predict", {
		method: "POST",
		body: formData,
	});

	const data = await res.json();
	result.innerText = `Class: ${data.class_name}`;
};

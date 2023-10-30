fetch("/contents.json")
  .then(response => response.text())
  .then(data => {
    const json = JSON.parse(data);
    console.log(json);
  });
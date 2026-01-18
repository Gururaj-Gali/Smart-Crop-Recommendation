function predictCrop() {
    let data = `N=${N.value}&P=${P.value}&K=${K.value}
    &temperature=${temperature.value}&humidity=${humidity.value}&ph=${ph.value}`;

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: data
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "🌾 Best Crop for You: " + data.crop;
    });
}



const MyApp = {
    initialize: () => {
        document.getElementById('id_release_date').addEventListener('change', () =>{
            console.log("change");
            MyApp.checkReleaseDate();
        });
    },

    checkReleaseDate: () =>{
        const releaseDateElement = document.getElementById("id_release_date");
        const inputDate = new Date(releaseDateElement.value);
        const today = new Date();

        if (inputDate > today) {
            releaseDateElement.setCustomValidity("¡La fecha no puede ser posterior a hoy!");
        } else {
            releaseDateElement.setCustomValidity("");
        }
    }
};

if (document.readyState === "loading") {
    document.addEventListener("readystatechange", (Event) => {
        if (Event.target.readyState === "interactive") {
            MyApp.initialize();
        }
    });
} else {
    MyApp.initialize();
}
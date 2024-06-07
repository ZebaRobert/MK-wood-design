let slideIndex = 0;
let slides = document.querySelectorAll(".slide");

function showSlides() {
    slides.forEach((slide, index) => {
        slide.style.display = index === slideIndex ? "block" : "none";
    });
}

document.querySelector(".prev").addEventListener("click", () => {
    slideIndex = (slideIndex - 1 + slides.length) % slides.length;
    showSlides();
});

document.querySelector(".next").addEventListener("click", () => {
    slideIndex = (slideIndex + 1) % slides.length;
    showSlides();
});

function refreshReviews() {
    fetch('/gallery/reviews/')
        .then(response => response.json())
        .then(data => {
            let reviewsBox = document.querySelector(".reviews-box");
            reviewsBox.innerHTML = "";
            data.reviews.forEach(review => {
                let reviewCard = `
                    <div class="review-card">
                        <h3>${review.author}</h3>
                        <p>Rating: ${review.rating}</p>
                        <p>${review.content}</p>
                        <small>${review.created_on}</small>
                    </div>`;
                reviewsBox.innerHTML += reviewCard;
            });
        });
}

setInterval(refreshReviews, 20000);  // Refresh reviews every 20 seconds

showSlides();


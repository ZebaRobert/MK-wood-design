 document.addEventListener("DOMContentLoaded", function(){

    // Review form submission
    const reviewForm = document.getElementById('review-form');
    const feedbackMessage = document.getElementById('feedback-message');

    if (reviewForm) {
        reviewForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(reviewForm);
            fetch(reviewForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    feedbackMessage.style.display = 'block';
                    setTimeout(() => {
                        feedbackMessage.style.display = 'none';
                        reviewForm.reset();
                    }, 3000);
                } else {
                    alert('There was an error submitting your review.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
 }) 

    


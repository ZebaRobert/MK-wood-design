 document.addEventListener("DOMContentLoaded", function(){
    console.log('Document is ready');

    // Review form submission
    const reviewForm = document.getElementById('review-form');
    const feedbackToast = document.getElementById('feedback-toast');
    const toastBody = feedbackToast ? feedbackToast.querySelector('.toast-body') : null;

    // Show toast if there are messages
    if (feedbackToast && !reviewForm && toastBody && toastBody.textContent.trim() !== '') {
        const toast = new bootstrap.Toast(feedbackToast);
        toast.show();
    }
 
     // Review form submission
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
                     const toast = new bootstrap.Toast(feedbackToast);
                     toast.show();
                     reviewForm.reset();
                 } else {
                     console.error('Error submitting review:', data.errors);
                 }
             })
             .catch(error => console.error('Error:', error));
         });
     }
});

    


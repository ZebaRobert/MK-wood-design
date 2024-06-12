document.addEventListener("DOMContentLoaded", function() {
    const editButton = document.getElementById('edit-button');
    const cancelButton = document.getElementById('cancel-button');
    const profileInfo = document.getElementById('profile-info');
    const profileForm = document.getElementById('profile-form');

    editButton.addEventListener('click', function() {
        profileInfo.style.display = 'none';
        profileForm.style.display = 'block';
    });

    cancelButton.addEventListener('click', function() {
        profileForm.style.display = 'none';
        profileInfo.style.display = 'block';
    });
});
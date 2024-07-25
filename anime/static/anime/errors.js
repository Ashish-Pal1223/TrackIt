document.addEventListener('DOMContentLoaded', function () {
    const errorDialogues = document.querySelectorAll('.error-dialogue');
    
    errorDialogues.forEach(dialogue => {
        if (dialogue.querySelector('.error-content p')) {
            dialogue.classList.add('show');
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var likeButtons = document.querySelectorAll(".like-btn");
    var dislikeButtons = document.querySelectorAll(".dislike-btn");
    var commentForm = document.getElementById("comment-form");

    likeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var locationId = this.getAttribute("data-location");
            updateLikes(locationId);
        });
    });

    dislikeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var locationId = this.getAttribute("data-location");
            updateDislikes(locationId);
        });
    });


    commentForm.addEventListener("submit", function (event) {
        event.preventDefault();
        var locationId = this.querySelector('.name').value;
        var commentText = this.querySelector('.commentBox').value;
        updateComments(locationId, commentText);
    });

    function updateComments(locationId, commentText) {
        fetch(`/main/add_comment/${locationId}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify({
                text: commentText
            })
        })
            .then(response => response.json())
            .then(data => {
                // Update comment count or display newly added comment
            });
    }

    function updateLikes(locationId) {
        fetch(`/main/like/${locationId}/`, {
            method: "GET"
        })
            .then(response => response.json())
            .then(data => {
                var likeCount = document.querySelector(`.like-count[data-location="${locationId}"]`);
                likeCount.textContent = data.likes;
            });
    }

    function updateDislikes(locationId) {
        fetch(`/main/dislike/${locationId}/`, {
            method: "GET"
        })
            .then(response => response.json())
            .then(data => {
                var dislikeCount = document.querySelector(`.dislike-count[data-location="${locationId}"]`);
                dislikeCount.textContent = data.dislikes;
            });
    }
});


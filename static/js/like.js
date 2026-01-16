document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".like-btn").forEach(button => {
    button.addEventListener("click", () => {

      const postId = button.dataset.postId;

      fetch(`/like/${postId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "X-Requested-With": "XMLHttpRequest"
        }
      })
      .then(response => response.json())
      .then(data => {

        // Update like count
        document.getElementById(`like-count-${postId}`).innerText =
          data.total_likes;

        // Update button text
        button.innerHTML = data.liked
          ? `💔 Unlike <span id="like-count-${postId}">${data.total_likes}</span>`
          : `❤️ Like <span id="like-count-${postId}">${data.total_likes}</span>`;
      });

    });
  });
});

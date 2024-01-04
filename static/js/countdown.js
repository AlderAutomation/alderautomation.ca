function updateTimer() {
    const promo_date = new Date(2024, 4, 26, 12, 0, 0);
    const now = new Date();
    const timeDifference = promo_date - now;

    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    const formattedTime = `${days} days, ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    document.querySelector(".time").innerHTML = formattedTime;
}

updateTimer();

setInterval(updateTimer, 1000);
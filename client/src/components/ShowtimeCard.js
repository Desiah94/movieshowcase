import React from 'react';

const ShowtimeCard = ({ showtime }) => {
  return (
    <div className="card">
      <div className="card-body">
        <h5 className="card-title">{showtime.time}</h5>
      </div>
    </div>
  );
};

export default ShowtimeCard;

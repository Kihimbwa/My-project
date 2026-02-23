import { useState } from "react";
import axios from "axios";

function BorrowForm({ book, onBorrowSuccess }) {
  const [expectedReturnDate, setExpectedReturnDate] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post(`http://127.0.0.1:8000/api/borrows/`, {
      book_id: book.id,
      expected_return_date: expectedReturnDate
    })
    .then(res => {
      alert("Book borrowed successfully!");
      onBorrowSuccess();
    })
    .catch(err => console.log(err));
  };

  return (
    <form onSubmit={handleSubmit} className="border p-4 rounded shadow mt-4">
      <label>Expected Return Date:</label>
      <input
        type="date"
        value={expectedReturnDate}
        onChange={e => setExpectedReturnDate(e.target.value)}
        className="border p-2 rounded w-full my-2"
        required
      />
      <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
        Borrow
      </button>
    </form>
  );
}

export default BorrowForm;
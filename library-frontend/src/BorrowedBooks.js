import { useEffect, useState } from "react";
import axios from "axios";
import ReturnBook from "./ReturnBook";

function BorrowedBooks() {
  const [borrows, setBorrows] = useState([]);

  const fetchBorrows = () => {
    axios.get("http://127.0.0.1:8000/api/borrows/")
      .then(res => setBorrows(res.data))
      .catch(err => console.log(err));
  };

  useEffect(() => {
    fetchBorrows();
  }, []);

  const handleReturnSuccess = () => {
    alert("Book returned successfully!");
    fetchBorrows(); // refresh list
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1 className="text-3xl font-bold mb-4">My Borrowed Books</h1>

      {borrows.length === 0 && <p>No borrowed books.</p>}

      {borrows.map(borrow => (
        <div key={borrow.id} className="border p-4 mb-4 rounded shadow">
          <h2 className="text-xl font-semibold">{borrow.book.title}</h2>
          <p>Author: {borrow.book.author}</p>
          <p>Borrow Date: {borrow.borrow_date}</p>
          <p>Expected Return: {borrow.expected_return_date}</p>
          <p>Actual Return: {borrow.actual_return_date || "Not returned"}</p>
          <p>Penalty: {borrow.penalty}</p>

          {!borrow.actual_return_date && (
            <ReturnBook borrow={borrow} onReturnSuccess={handleReturnSuccess} />
          )}
        </div>
      ))}
    </div>
  );
}

export default BorrowedBooks;
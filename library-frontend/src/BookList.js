import { useEffect, useState } from "react";
import axios from "axios";

function BookList({ onSelectBook }) {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/books/")
      .then(res => setBooks(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1 className="text-3xl font-bold mb-4">Library Books</h1>
      {books.map(book => (
        <div key={book.id} className="border p-4 mb-4 rounded shadow">
          <h2 className="text-xl font-semibold">{book.title}</h2>
          <p>Author: {book.author}</p>
          <p>Genre: {book.genre}</p>
          <p>Available Copies: {book.available_copies}</p>
          <button
            onClick={() => onSelectBook(book)}
            className="mt-2 px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
            disabled={book.available_copies === 0}
          >
            {book.available_copies > 0 ? "Borrow Book" : "No Copies"}
          </button>
        </div>
      ))}
    </div>
  );
}

export default BookList;
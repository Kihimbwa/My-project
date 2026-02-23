function BookDetail({ book, onBack }) {
  if (!book) return null;

  return (
    <div style={{ padding: "20px" }}>
      <button onClick={onBack} className="mb-4 px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700">
        Back
      </button>

      <h1 className="text-3xl font-bold mb-2">{book.title}</h1>
      <p><strong>Author:</strong> {book.author}</p>
      <p><strong>Genre:</strong> {book.genre}</p>
      <p><strong>ISBN:</strong> {book.isbn}</p>
      <p><strong>Publication Date:</strong> {book.publication_date}</p>
      <p><strong>Available Copies:</strong> {book.available_copies}</p>
    </div>
  );
}

export default BookDetail;
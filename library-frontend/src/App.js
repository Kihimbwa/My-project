import { useState } from "react";
import BookList from "./BookList";
import BookDetail from "./BookDetail";
import BorrowForm from "./BorrowForm";
import BorrowedBooks from "./BorrowedBooks";

function App() {
  const [selectedBook, setSelectedBook] = useState(null);
  const [borrowStep, setBorrowStep] = useState(false);
  const [viewBorrowed, setViewBorrowed] = useState(false);

  const handleSelectBook = (book) => {
    setSelectedBook(book);
    setBorrowStep(true);
  };

  const handleBorrowSuccess = () => {
    setSelectedBook(null);
    setBorrowStep(false);
  };

  const handleBack = () => {
    setSelectedBook(null);
    setBorrowStep(false);
  };

  return (
    <div className="container mx-auto p-4">
      {!viewBorrowed && !selectedBook && (
        <>
          <button
            onClick={() => setViewBorrowed(true)}
            className="mb-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            View My Borrowed Books
          </button>
          <BookList onSelectBook={handleSelectBook} />
        </>
      )}

      {selectedBook && !borrowStep && <BookDetail book={selectedBook} onBack={handleBack} />}
      {selectedBook && borrowStep && <BorrowForm book={selectedBook} onBorrowSuccess={handleBorrowSuccess} />}
      {viewBorrowed && (
        <>
          <button
            onClick={() => setViewBorrowed(false)}
            className="mb-4 px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700"
          >
            Back to Book List
          </button>
          <BorrowedBooks />
        </>
      )}
    </div>
  );
}

export default App;
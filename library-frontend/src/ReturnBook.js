import axios from "axios";

function ReturnBook({ borrow, onReturnSuccess }) {
  const handleReturn = () => {
    axios.post(`http://127.0.0.1:8000/api/borrows/${borrow.id}/return_book/`)
      .then(res => {
        alert("Book returned successfully!");
        onReturnSuccess();
      })
      .catch(err => console.log(err));
  };

  return (
    <button
      onClick={handleReturn}
      className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
    >
      Return Book
    </button>
  );
}

export default ReturnBook;
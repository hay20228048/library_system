import BorrowButton from "./BorrowButton";

async function getBooks() {
  const res = await fetch("http://localhost:3000/api/books", {
    cache: "no-store",
  });

  return res.json();
}

export default async function BooksPage() {
  const books = await getBooks();

  return (
    <div>
      <h1>Books</h1>
      <ul>
        {books.map((book: any) => (
          <li key={book.book_id}>
            {book.title} - {book.author}
            <BorrowButton bookId={book.book_id} />
          </li>
        ))}
      </ul>
    </div>
  );
}
import DeleteButton from "./DeleteButton";
import Link from "next/link";

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
      <Link href="/books/create">Add Book</Link>

      <ul>
        {books.map((book: any) => (
          <li key={book.book_id}>
            {book.title} - {book.author}
            <Link href={`/books/edit/${book.book_id}`}> Edit </Link>
            <DeleteButton id={book.book_id} />
          </li>
        ))}
      </ul>
    </div>
  );
}
import BookForm from "../../BookForm";

async function getBook(id: string) {
  const res = await fetch(`http://localhost:3000/api/books`);
  const books = await res.json();
  return books.find((b: any) => b.book_id === Number(id));
}

export default async function EditBookPage({
  params,
}: {
  params: { id: string };
}) {
  const book = await getBook(params.id);

  return (
    <div>
      <h1>Edit Book</h1>
      <BookForm initialData={book} bookId={params.id} />
    </div>
  );
}
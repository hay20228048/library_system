"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function BookForm({
  initialData,
  bookId,
}: {
  initialData?: any;
  bookId?: string;
}) {
  const router = useRouter();

  const [title, setTitle] = useState(initialData?.title || "");
  const [author, setAuthor] = useState(initialData?.author || "");

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    const method = bookId ? "PUT" : "POST";
    const url = bookId ? `/api/books/${bookId}` : "/api/books";

    await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, author }),
    });

    router.push("/books");
    router.refresh();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        placeholder="Author"
        value={author}
        onChange={(e) => setAuthor(e.target.value)}
      />
      <button type="submit">
        {bookId ? "Update" : "Create"}
      </button>
    </form>
  );
}
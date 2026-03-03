"use client";

import { useRouter } from "next/navigation";

export default function DeleteButton({ id }: { id: number }) {
  const router = useRouter();

  const handleDelete = async () => {
    await fetch(`/api/books/${id}`, {
      method: "DELETE",
    });

    router.refresh();
  };

  return <button onClick={handleDelete}>Delete</button>;
}
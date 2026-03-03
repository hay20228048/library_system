"use client";

import { useState } from "react";

export default function BorrowButton({ bookId }: { bookId: number }) {
  const [memberId, setMemberId] = useState("");

  const handleBorrow = async () => {
    await fetch("/api/borrow", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        book_id: bookId,
        member_id: Number(memberId),
      }),
    });

    alert("Book borrowed!");
  };

  return (
    <div>
      <input
        placeholder="Member ID"
        value={memberId}
        onChange={(e) => setMemberId(e.target.value)}
      />
      <button onClick={handleBorrow}>Borrow</button>
    </div>
  );
}
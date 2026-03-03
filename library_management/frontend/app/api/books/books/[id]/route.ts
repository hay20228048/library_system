export async function PUT(
  request: Request,
  { params }: { params: { id: string } }
) {
  const body = await request.json();

  const res = await fetch(`http://api:8000/books/${params.id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  return Response.json(await res.json());
}

export async function DELETE(
  request: Request,
  { params }: { params: { id: string } }
) {
  await fetch(`http://api:8000/books/${params.id}`, {
    method: "DELETE",
  });

  return Response.json({ message: "Deleted" });
}
export async function GET() {
  const res = await fetch("http://api:8000/books", {
    cache: "no-store",
  });

  return Response.json(await res.json());
}

export async function POST(request: Request) {
  const body = await request.json();

  const res = await fetch("http://api:8000/books", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  return Response.json(await res.json());
}
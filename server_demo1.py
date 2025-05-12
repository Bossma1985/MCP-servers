from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Suma dos números enteros y devuelve el resultado"""
    return a + b

@mcp.tool()
def celcius_to_fahrenheit(c: float) -> float:
    """Convierte grados Celcius a Fahrenheit"""
    return c * 9/5 + 32

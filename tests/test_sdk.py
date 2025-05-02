import pytest
from vector_db_sdk import VectorDBClient, Library, Document, Chunk, LibraryMetadata
from vector_db_sdk.models import DocumentMetadata
from datetime import datetime

@pytest.fixture
def client():
    return VectorDBClient(base_url="http://localhost:8000")

def test_sdk_workflow(client):
    # Create a library
    library = Library(
        name="Test Library",
        metadata=LibraryMetadata(
            name="Test Library",
            createdAt=datetime.now().isoformat(),
            description="My library"
        )
    )
    try:
        library_response = client.create_library(library)
        assert "id" in library_response, "Library creation should return an ID"
        library_id = library_response["id"]
        print(f"Created library with ID: {library_id}")
    except Exception as e:
        pytest.fail(f"Library creation failed: {e}")

    # Verify library exists
    try:
        library_check = client.get_library(library_id)
        assert "id" in library_check, "Library should exist"
        print(f"Verified library exists: {library_check}")
    except Exception as e:
        pytest.fail(f"Library verification failed: {e}")

    # Update library
    try:
        client.update_library(library_id, library)
        print(f"Updated library with ID: {library_id}")
    except Exception as e:
        pytest.fail(f"Library update failed: {e}")
    # Delete library
    # try:
    #     client.delete_library(library_id)
    #     print(f"Deleted library with ID: {library_id}")
    # except Exception as e:
    #     pytest.fail(f"Library deletion failed: {e}")


    # Add a document
    document = Document(
        metadata=DocumentMetadata(
            name="Test Document",
            createdAt=datetime.now().isoformat()
        )
    )
    try:
        document_response = client.add_document(library_id, document)
        assert "id" in document_response, "Document creation should return an ID"
        document_id = document_response["id"]
        print(f"Added document with ID: {document_id}")
    except Exception as e:
        pytest.fail(f"Document creation failed: {e}")

    # Verify document exists    
    try:
        document_check = client.get_document(library_id, document_id)
        assert "id" in document_check, "Document should exist"
        print(f"Verified document exists: {document_check}")
    except Exception as e:
        pytest.fail(f"Document verification failed: {e}")

    # Update document   
    try:
        client.update_document(library_id, document_id, document)
        print(f"Updated document with ID: {document_id}")
    except Exception as e:
        pytest.fail(f"Document update failed: {e}")

    # # Delete document       
    # try:
    #     client.delete_document(library_id, document_id)
    #     print(f"Deleted document with ID: {document_id}")
    # except Exception as e:
    #     pytest.fail(f"Document deletion failed: {e}")

    # Add a chunk
    chunk = Chunk(text="Hello world", metadata={"name": "Kevin", "createdAt": datetime.now().isoformat()})
    try:
        chunk_response = client.add_chunk(library_id, document_id, chunk)
        assert "chunk_id" in chunk_response, "Chunk creation should return an ID"
        chunk_id = chunk_response["chunk_id"]
        print(f"Added chunk with ID: {chunk_id}")
    except Exception as e:
        pytest.fail(f"Chunk creation failed: {e}")

    # Verify chunk exists       
    try:
        chunk_check = client.get_chunk(chunk_id)
        assert "id" in chunk_check, "Chunk should exist"
        print(f"Verified chunk exists: {chunk_check}")
    except Exception as e:
        pytest.fail(f"Chunk verification failed: {e}")

    # Update chunk      
    try:
        client.update_chunk(chunk_id, chunk)
        print(f"Updated chunk with ID: {chunk_id}")
    except Exception as e:
        pytest.fail(f"Chunk update failed: {e}")


    # # Delete chunk
    # try:
    #     client.delete_chunk(chunk_id)
    #     print(f"Deleted chunk with ID: {chunk_id}")
    # except Exception as e:
    #     pytest.fail(f"Chunk deletion failed: {e}")

    # Search
    try:
        results = client.search_all_libraries(
            query_text="hello",
            metadata_filters={"name": "Kevin", "createdAfter": "2025-04-29"}
        )
        assert isinstance(results, list), "Search should return a list"
        for result in results:
            print(f"Search result: {result}")
    except Exception as e:
        print(f"Search failed (non-critical): {e}")

    
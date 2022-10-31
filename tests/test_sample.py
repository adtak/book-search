from book_search.monkey import depends, sample1, sample2


# functionをimportしている場合はモックされない
def test_sample1_ng(monkeypatch):
    mock_text = "This is mock"
    monkeypatch.setattr(depends, "get_text", lambda: mock_text)
    assert sample1.my_function() != mock_text


# moduleをimportしている場合はモックできる
def test_sample2_ok(monkeypatch):
    mock_text = "This is mock"
    monkeypatch.setattr(depends, "get_text", lambda: mock_text)
    assert sample2.my_function() == mock_text


# functionをimportしている場合はテスト対象にimportされたものをモックする
def test_sample1_ok(monkeypatch):
    mock_text = "This is mock"
    monkeypatch.setattr(sample1, "get_text", lambda: mock_text)
    assert sample1.my_function() == mock_text

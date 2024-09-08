from django.test import TestCase

# Crie seus testes aqui.

# Exemplo de teste para a view PostView
class PostViewTest(TestCase):
    def test_get(self):
        # Faz uma requisição GET para a URL /home/
        response = self.client.get('/home/')
        # Verifica se a resposta tem status 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verifica se o conteúdo da resposta é "Hello World!"
        self.assertContains(response, "Hello World!")

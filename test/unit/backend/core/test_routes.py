import unittest
from django.test import TestCase, Client
from modules.user.models import User


class StatusCode:
    """ Status de sucesso na requisicao """
    request_success = 200
    #201 Criado (Created)
    #202 Aceito (Accepted)
    #203 Informação não autorativa (Non-Authorative Information)
    #204 Sem conteúdo (No Content)
    #205 Conteúdo apagado (Reset Content)
    #206 Conteúdo parcial (Partial Content)

    """ Status de redirecionamentos na requisicao """
    #300 Escolhas múltiplas (Multiple Choices)
    request_redirected_permanently = 301 # Mudado permanentemente (Moved Permanently), provavelmente por conta de uma '/' no final da rota.
    request_redirected             = 302 # Mudado temporariamente (Moved Temporarily)
    #303 Veja outras (See Other)
    #304 Não modificado (Not Modified)
    #305 Use Proxy (Use Proxy)

    """ Status de erro na requisições """
    request_bad = 400 # Requisição viciada (Bad Request)
    request_authorization_required = 401 # Autorização Requerida (Authorization Required)
    request_payment_required       = 402 # Pagamento Requerido (Payment Required)
    request_forbidden              = 403 # Proibido (Forbidden)
    request_not_found              = 404  # Não encontrado (Not Found)
    #405 Método não permitido (Method Not Allowed)
    #406 Codificação não aceita (Not Acceptable (encoding)
    #407 Autenticação proxy Requerida (Proxy Authentication Required )
    #408 Requisição vencida (Request Timed Out)
    #409 Requisição conflitante (Conflicting Request)
    #410 Acabou (Gone)
    #411 Requer comprimento do conteúdo (Content Length Required)
    #412 Falha na precondição (Precondition Failed)
    #413 Entidade requerida muito longa (Request Entity Too Long)
    #414 URI requerida muito longa (Request URI Too Long)
    #415 Tipo de mídia não suportado (Unsupported Media Type)

    """ Status de erro no Servidor """
    request_internal_error = 500 # Erro interno do servidor (Internal Server Error)
    #501 Não implementado (Not Implemented)
    #502 Gateway viciado (Bad Gateway)
    #503 Serviço não disponível (Service Unavailable)
    #504 Gateway vencido (Gateway Timeout)
    #505 Versão HTTP não suportada (HTTP Version Not Supported)


class NewBaseRoutesTest(object):
    """
        public_routes: Rotas de peginas publico.
        private_routes: Rotas de pagina restritas.

        public_api: Rotas de servicos de acesso publico.
        private_api: Rotas de servicos de acesso restrito.
        protected_api: Rotas de servicos nao restrito mas que exigem protecao por token.
    """
    private_routes = []
    public_routes = []

    public_api = []
    private_api = []
    protected_api = []

    def setUp(self):
        super(NewBaseRoutesTest, self).setUp()

    def request_url(self, url):
        request = self.client.get(url)
        return request

    def login(self, email, senha):
        self.user = User.objects.create_test_user(email, senha)
        self.client.login(username=email, password=senha)
        return self.user

    def logout(self):
        self.client.logout()

    def test_private_routes_with_anonymous_user(self):
        for url in self.private_routes:
            self.assertNotEqual(self.request_url(url).status_code, StatusCode.request_success,  "Teste com acesso a rotas privada com usuario anonimo. (OK)")

    def test_private_routes_with_autenticated_user(self):
        self.login('teste@gmail.com','teste123')
        for item in self.private_routes:
            self.assertEqual(self.request_url(item).status_code, StatusCode.request_success, "Teste com acesso a rotas privada com usuario autenticado. (OK)")
        self.logout()

    def test_post_private_api_with_autenticated_user(self):
        user = self.login('usuario@teste.com', '1q2w3e4r')
        for item in self.private_api:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertEqual(result.status_code,StatusCode.request_success, "Teste com envio de dados para api privada com usuario autenticado. (OK)")
        self.logout()

    def test_post_private_api_with_anonymous_user(self):
        self.logout()
        for item in self.private_api:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertNotEqual(result.status_code,StatusCode.request_success, "Teste com envio de dados para api privada com usuario anonimo. (OK)")

    def test_post_private_api_without_csrf_token(self):
        self.client = Client(enforce_csrf_checks=True)
        user = self.login('usuario@teste.com', '1q2w3e4r')
        for item in self.private_api:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertNotEqual(result.status_code, StatusCode.request_success, "Teste com envio de dados para api privada com usuario autenticado. (OK)")
        self.logout()
        user.delete()

    def test_post_protected_api(self):
        #user = self.login('usuario@teste.com', '1q2w3e4r')
        self.logout()
        for item in self.protected_api:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertEqual(result.status_code,StatusCode.request_success, "Teste com envio de dados para api privada com usuario autenticado. (OK)")

    def test_post_protected_api_without_csrf_token(self):
        self.client = Client(enforce_csrf_checks=True)
        self.logout()
        for item in self.protected_api:
            result = self.client.post(item[0], data=item[1], HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            self.assertNotEqual(result.status_code,StatusCode.request_success, "Teste com envio de dados para api privada com usuario autenticado. (OK)")

    def test_public_routes(self):
        for url in self.private_routes:
            self.assertNotEqual(self.request_url(url).status_code, StatusCode.request_success)

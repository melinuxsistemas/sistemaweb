/**
 * Created by lucas on 20/10/2017.
 */
var application = angular.module('modules.perms',[]);
application.controller('permission_controller', function($scope) {

	$scope.list_menu_Compras = ['Pedido e Fornecedoras','Lista para Reposição,',
		'Pedidos para Cotação','Entrada de Mercadorias',
		'Aquisição de Serviços','Corrigir Entrada','Devolução e Fornecedores',
		'Manifesto e Recusa NF-e','Histórico de Compras'];

	$scope.list_menu_Vendas = ['Manuntenção de Preços','Terminal Caixa','Venda Balcão,' ,
		'Tele-Vendas','Carteira de Pedidos','Faturamento','Devolução de Vendas','Historico de vendas'];

	$scope.list_menu_Servicos = ['Grupo de Serviços','Cadastro de Serviço','Chamados Técnicos',
		'Serviços de Locação','Serviços de Logística','Representação Comercial'];

	$scope.list_menu_Outras_operacoes = ['Tranferências','Ordem de Abastecimento','Desmembrametos',
		'Produção','Digitação de Balanço','Notas de Simples Remessa','Emissão de Notas Avulsas',
		'Controle de Frota'];

	$scope.list_menu_Financas = ['Programação Financeira','Lançamento de Guias','Liberar Comissões',
		'Tesouraria','Vale para Funcionários','Empréstimos e Vales'];

	$scope.list_menu_Supervisao_vendas = ['Locais Atendidos','Segmentos Atendidos','Carteiras de Venda',
		'Rota de Entrega','Motivos de Devolução','Liberar Comissões','Análise de Vendas',];

	$scope.list_menu_Gerencia = ['Empresas do Grupo','Funcionários/Usuários',
		'Cadastros Gerências','Formas de Recebimento','Plano de Contas','Contratos',
		'Análises Gerenciais','Histórico de Produtos','Altrações Manuais'];

	$scope.list_menu_Contabil = ['Configurações Fiscais','Modelo de Documento','Tributação Produtos',
		'Gerar Arquivos Governo','Ánalise Tributária','Planilha Sub. Tributária']



	$scope.select_perm = function ($scope) {
		var selected = 1;
		select_rating('rating_permission', selected)
		//var teste = document.querySelector('input[name="ratingtwo"]:checked').value
		//alert(tesste);
		//document.querySelector('input[name="ratingtwo"]:checked').value=3
		$scope.$apply();
	}
});


/**
 * Created by lucas on 20/10/2017.
 */
var application = angular.module('modules.perms',[]);
application.controller('permission_controller', function($scope) {
	$scope.list_menu_Cadastros = ['Entidades','Permissões','Grupos Mercadológicos',
		'Produtos','Vinculos de Produtos','Agenda Telefônica','Tabelas Auxíliares']

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

	$scope.lista_all_menus = [
			$scope.list_menu_Cadastros,$scope.list_menu_Compras,$scope.list_menu_Contabil,
			$scope.list_menu_Financas,$scope.list_menu_Gerencia,$scope.list_menu_Outras_operacoes,
			$scope.list_menu_Supervisao_vendas,$scope.list_menu_Vendas,$scope.list_menu_Servicos
	]



	$scope.select_perm = function ($scope) {
		var selected = 1;
		select_rating('rating_permission', selected)
		//var teste = document.querySelector('input[name="ratingtwo"]:checked').value
		//alert(tesste);
		//document.querySelector('input[name="ratingtwo"]:checked').value=3
		$scope.$apply();
	}

	$scope.load_all = function () {
		alert("Vindo aquie e entando preencher")
		var list_respost = [
				[1,1,1,1,1,1,1],
				[2,2,2,2,2,2,2,2,2],
				[3,3,3,3,3,3,3,3],
				[0,0,0,0,0,0],
				[1,1,1,1,1,1,1,1],
				[0,0,0,0,0,0],
				[3,3,3,3,3,3,3],
				[0,0,0,0,1,1,1,1,3],
				[3,3,3,3,3,0]
		]
		select_rating($scope.list_menu_Cadastros[0], 3)
		for (i = 0;i < list_respost.size();i++){
			for (j = 0; j <list_respost[i];j++){
				select_rating($scope.lista_all_menus[i][j],list_respost[i][j])
			}
		}


	}
});


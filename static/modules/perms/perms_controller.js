/**
 * Created by lucas on 20/10/2017.
 */
var application = angular.module('modules.perms',[]);
application.controller('permission_controller', function($scope) {
	/*Menus do Sistema com Label e ID*/
	$scope.list_menu_Cadastros = [
		{label: 'Entidades',id:'entidade'},
		{label:'Permissões',id:'permissoes'},
		{label:'Grupos Mercadológicos',id:'grupos_mercadologicos'},
		{label:'Produtos', id:'produtos'},
		{label:'Vinculos de Produtos',id:'vinculos_de_produtos'},{label:'Agenda Telefônica',id:'agenda_telefonica'},
		{label:'Tabelas Auxíliares',id:'tabelas_auxiliares'}
		];

	$scope.list_menu_Compras = [
		{label:'Pedido e Fornecedoras', id:'pedido_e_fornecedores'},
		{label:'Lista para Reposição',id:'lista_reposicao'},
		{label: 'Pedidos para Cotação', id:'pedidos_cotacao'},
		{label: 'Entrada de Mercadorias', id:'entrada_mercadorias'},
		{label: 'Aquisição de Serviços', id:'aquisicao_servicos'},
		{label: 'Corrigir Entrada', id:'corrigir_entrada'},
		{label: 'Devolução e Fornecedores', id:'devolucao_fornecedores'},
		{label: 'Manifesto e Recusa NF-e', id:'manifesto_recusa'},
		{label: 'Histórico de Compras', id:'historico_compras'}];

	$scope.list_menu_Vendas = [
		{label:'Manuntenção de Preços',id:'manuntencao_precos'},
		{label:'Terminal Caixa',id:'terminal_caixa'},
		{label:'Venda Balcão',id:'venda_balcao'},
		{label:'Tele-Vendas',id:'tele_vendas'},
		{label:'Carteira de Pedidos',id:'carteira_pedidos'},
		{label:'Faturamento',id:'faturamento'},
		{label:'Devolução de Vendas',id:'devolucao_vendas'},
		{label:'Histórioco de Vendas',id:'historico_vendas'}
		];

	$scope.list_menu_Servicos = [
		{label:'Grupo de Serviços',id:'grupo_servicos'},
		{label:'Cadastro de Serviço',id:'cadastro_servico'},
		{label:'Chamados Técnicos',id:'chamados_tecnicos'},
		{label:'Serviços de Locação',id:'servicos_locacao'},
		{label:'Serviços de Logística',id:'servicos_logistica'},
		{label:'Representação Comercial',id:'representacao_comercial'}
		];

	$scope.list_menu_Outras_operacoes = [
			{label:'Tranferências',id:'transferencias'},
	{label:'Ordem de Abastecimento',id:'ordem_abastecimento'},
	{label:'Desmembrametos',id:'desmembramentos'},
	{label:'Produção',id:'producao'},
	{label:'Digitação de Balanço',id:'digitacao_balanco'},
	{label:'Notas de Simples Remessa',id:'notas_simples_remessa'},
	{label:'Emissão de Notas Avulsas',id:'emissao_notas_avulsas'},
	{label:'Controle de Frota',id:'controle_frota'}];

	$scope.list_menu_Financas = [{label:'Programação Financeira',id:'programacao_financeira'},
		{label:'Lançamento de Guias',id:'lancamentos_guias'},
		{label:'Liberar Comissões',id:'liberar_comissoes'},
		{label:'Tesouraria',id:'tesouraria'},
		{label:'Vale para Funcionários',id:'vale_funcionarios'},
		{label:'Empréstimos e Vales',id:'emprestimo_vales'}
		];

	$scope.list_menu_Supervisao_vendas = [{label:'Locais Atendidos',id:'locais_atentidos'},
		{label:'Segmentos Atendidos',id:'segmentos_atendidos'},
		{label:'Carteiras de Venda',id:'carteiras_vendas'},
		{label:'Rota de Entrega',id:'rota_entrega'},
		{label:'Motivos de Devolução',id:'motivos_devolucao'},
		/*Duplicidade de Menu*/
		{label:'Liberar Comissões',id:'liberar_comissoes_2'},
		{label:'Análise de Vendas',id:'analise_vendas'}
		];

	$scope.list_menu_Gerencia = [
		{label:'Empresas do Grupo',id:'empresas_grupo'},
		{label:'Funcionários/Usuários',id:'funcinarios_usuarios'},
		{label:'Cadastros Gerências',id:'cadastro_gerencias'},
		{label:'Formas de Recebimento',id:'formas_recebimento'},
		{label:'Plano de Contas',id:'plano_contas'},
		{label:'Contratos',id:'contratos'},
		{label:'Análises Gerenciais',id:'analise_gerencial'},
		{label:'Histórico de Produtos',id:'hitorico_produtos'},
		{label:'Altrações Manuais',id:'alteracoes_manuais'}];

	$scope.list_menu_Contabil = [{label:'Configurações Fiscais',id:'configuracoes_fiscais'},
		{label:'Modelo de Documento',id:'modelo_documento'},
		{label:'Tributação Produtos',id:'tributacao_produtos'},
		{label:'Gerar Arquivos Governo',id:'gerar_arq_governo'},
		{label:'Ánalise Tributária',id:'analise_tributaria'},
		{label:'Planilha Sub. Tributária',id:'planilha_sub_tributaria'}];

	/*Lista com todos Menus*/
	$scope.lista_all_menus = [
			$scope.list_menu_Cadastros,$scope.list_menu_Compras,$scope.list_menu_Vendas,
			$scope.list_menu_Servicos,$scope.list_menu_Outras_operacoes,$scope.list_menu_Financas,
			$scope.list_menu_Supervisao_vendas,$scope.list_menu_Gerencia,$scope.list_menu_Contabil
	]



	$scope.select_perm = function (id) {
		alert("Vindo;"+id)
		var selected = 1;
		//select_rating('rating_permission', selected)
		//var teste = document.querySelector('input[name="ratingtwo"]:checked').value
		//alert(tesste);
		//document.querySelector('input[name="ratingtwo"]:checked').value=3
		$scope.$apply();
	}

	$scope.load_all = function () {

		var list_respost = [
				[1,1,1,1,1,1,1],
				[2,2,2,2,2,2,2,2,2],
				[2,2,2,3,3,3,3,3],
				[0,0,0,0,0,0],
				[1,1,1,1,1,1,1,1],
				[0,0,0,0,0,0],
				[0,1,2,3,3,3,3],
				[0,0,0,0,1,1,1,1,3],
				[3,3,3,3,3,0]
		]
		//select_rating($scope.list_menu_Cadastros[1], 3)

		for (var i = 0;i < list_respost.length;i++){
			for (var j = 0; j <list_respost[i].length;j++){
				select_rating($scope.lista_all_menus[i][j].id,list_respost[i][j])
			}
		}
	}
});


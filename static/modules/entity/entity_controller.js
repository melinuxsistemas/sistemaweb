/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.entity', []);


application.controller('register_person_controller', function($scope) {
    $scope.cpf_cnpj = "";
    $scope.entity_name = "";
    $scope.fantasy_name = "";
    $scope.birth_date_foundation = "";

    $scope.save_person = function () {
        $scope.cpf_cnpj = $('#cpf_cnpj').val();
        $scope.birth_date_foundation = $('#birth_date_foundation').val();
        var data_paramters = {
            entity_type: 'PF',
            cpf_cnpj: clear_mask_numbers($scope.cpf_cnpj),
            entity_name: $scope.entity_name,
            fantasy_name: $scope.fantasy_name,
            birth_date_foundation: $scope.birth_date_foundation,
        }
        success_function = function (message) {
            check_response_message_form('#form-save-entity', message);
            alert("Beleza")
        }

        fail_function = function (message) {
            check_response_message_form('#form-save-entity', message);
            notify('error', 'Formulário com dados inválidos', 'Verifique os dados informado.')
        }
        request_api("/api/entity/register/person/save", data_paramters, validate_form_regiter_person, success_function, fail_function)

    }
});

application.controller('register_company_controller', function ($scope) {
    $scope.cpf_cnpj = "";
    $scope.entity_name = "";
    $scope.fantasy_name = "";
    $scope.birth_date_foundation = "";

    $scope.save_company = function () {
        $scope.cpf_cnpj = $('#cpf_cnpj').val();
        $scope.birth_date_foundation = $('#birth_date_foundation').val();
        var data_paramters = {
            entity_type: 'PJ',
            cpf_cnpj: clear_mask_numbers($scope.cpf_cnpj),
            entity_name: $scope.entity_name,
            fantasy_name: $scope.fantasy_name,
            birth_date_foundation: $scope.birth_date_foundation,
        }
        success_function = function (message) {
            check_response_message_form('#form-save-company', message);
            alert("Beleza")
        }

        fail_function = function (message) {
            check_response_message_form('#form-save-company', message);
            notify('error', 'Formulário com dados inválidos', 'Verifique os dados informado.')
        }
        request_api("/api/entity/register/company/save", data_paramters, validate_form_regiter_company, success_function, fail_function)

    };
});

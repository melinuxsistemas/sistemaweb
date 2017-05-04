/**
 * Created by diego on 03/05/2017.
 */
QUnit.module('qunit.tests', {

});

QUnit.test("terminate", function( assert ) {
  NProgress.done();
  assert.ok(true == true, "OK" );
});

-- company
INSERT INTO "main"."Account_company" ("id", "name", "corporation", "is_activate") VALUES ('1', '公司1', '1', '1');
INSERT INTO "main"."Account_company" ("id", "name", "corporation", "is_activate") VALUES ('2', '公司2', '1', '1');
INSERT INTO "main"."Account_company" ("id", "name", "corporation", "is_activate") VALUES ('3', '公司3', '1', '1');
INSERT INTO "main"."Account_company" ("id", "name", "corporation", "is_activate") VALUES ('4', '公司4', '1', '1');
INSERT INTO "main"."Account_company" ("id", "name", "corporation", "is_activate") VALUES ('5', '公司5', '1', '1');
INSERT INTO "main"."Account_company" ("id", "name", "corporation", "is_activate") VALUES ('6', '公司6', '1', '1');
INSERT INTO "main"."Account_company" ("id", "name", "corporation", "is_activate") VALUES ('7', '公司7', '1', '1');


-- BusinessScope
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('1', '经营分类1');
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('2', '经营分类2');
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('3', '经营分类3');
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('4', '经营分类4');
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('5', '经营分类5');
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('6', '经营分类6');
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('7', '经营分类7');
INSERT INTO "main"."Account_businessscope" ("id", "name") VALUES ('8', '经营分类8');

-- BusinessCompany
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('1', '买方公司1', '1', '9000', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('2', '买方公司2', '1', '9000', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('3', '买方公司3', '1', '8900', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('4', '买方公司4', '1', '12000', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('5', '买方公司5', '1', '0', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('6', '买方公司6', '1', '0', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('7', '买方公司7', '1', '5000', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('8', '买方公司8', '1', '0', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('9', '买方公司9', '1', '4000', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('10', '买方公司10', '1', '6000', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('11', '买方公司10', '1', '6000', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('12', '买方公司11', '1', '9900', '2');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('13', '买方公司12', '1', '12300', '4');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('14', '买方公司13', '1', '23000', '2');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('15', '买方公司14', '1', '0', '2');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('16', '卖方公司1', '1', '12200', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('17', '卖方公司2', '1', '34400', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('18', '卖方公司3', '1', '77700', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('19', '卖方公司4', '1', '9900', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('20', '卖方公司5', '1', '8800', '1');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('21', '卖方公司6', '1', '0', '2');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('22', '卖方公司7', '1', '12300', '2');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('23', '卖方公司8', '1', '33300', '5');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('24', '卖方公司9', '1', '11100', '6');
INSERT INTO "main"."Account_businesscompany" ("id", "name", "is_activate", "total_max_limit", "scope_id") VALUES ('25', '卖方公司10', '1', '9500', '7');


-- Buyer

INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('1', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('2', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('3', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('4', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('5', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('6', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('7', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('8', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('9', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('10', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('11', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('12', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('13', '2');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('14', '1');
INSERT INTO "main"."Account_buyer" ("businesscompany_ptr_id", "company_id") VALUES ('15', '4');

-- seller
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('16');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('17');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('18');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('19');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('20');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('21');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('22');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('23');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('24');
INSERT INTO "main"."Account_seller" ("businesscompany_ptr_id") VALUES ('25');

-- account
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('1', '买方公司1', '1111112212121', '建设银行', '123456', '1');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('2', '买方公司2', '124214325', '工商银行', '1312412', '2');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('3', '买方公司3', '1222222244', '平安银行', '3252323', '3');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('4', '买方公司4', '1115121121', '工商银行', '123456', '4');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('5', '买方公司5', '122287876244', '平安银行', '3252323', '5');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('6', '买方公司6', '111655121121', '工商银行', '1312412', '6');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('7', '买方公司7', '1123612212121', '建设银行', '123456', '7');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('8', '买方公司8', '1113325121121', '平安银行', '1312412', '8');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('9', '买方公司1', '1189615121121', '平安银行', '3252323', '9');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('10', '买方公司10', '11231512112169', '工商银行', '123456', '10');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('11', '买方公司10', '11231512112169', '工商银行', '123456', '11');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('12', '买方公司11', '1264522244', '工商银行', '123456', '12');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('13', '买方公司12', '1116955221121', '建设银行', '123456', '13');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('14', '买方公司13', '1112972212121', '工商银行', '1312412', '14');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('15', '买方公司14', '12227644244', '工商银行', '123456', '15');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('16', '卖方公司1', '126887876244', '建设银行', '1312412', '16');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('17', '卖方公司2', '127875463444', '建设银行', '1312412', '17');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('18', '卖方公司3', '12298777244', '工商银行', '1312412', '18');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('19', '卖方公司4', '11431655121121437', '建设银行', '123456', '19');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('20', '卖方公司5', '122286857876244', '建设银行', '1312412', '20');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('21', '卖方公司6', '1114756812121', '建设银行', '123456', '21');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('22', '卖方公司7', '12567545244', '工商银行', '1312412', '22');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('23', '卖方公司8', '15475685771', '平安银行', '1312412', '23');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('24', '卖方公司9', '111345421121', '工商银行', '123456', '24');
INSERT INTO "main"."Account_account" ("id", "account_name", "account", "bank_name", "bank_code", "businesscompany_id") VALUES ('25', '卖方公司10', '11675332421', '工商银行', '1312412', '25');
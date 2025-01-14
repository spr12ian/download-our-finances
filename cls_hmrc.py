from cls_helper_log import LogHelper
from cls_helper_sql import SQL_Helper
from cls_hmrc_people import HMRC_People
from tables import *
import utility_functions as uf


class HMRC:
    ONLINE_REPORT = "Online"
    PRINTED_REPORT = "Printed Form"
    REPORTS = [ONLINE_REPORT, PRINTED_REPORT]

    def __init__(self, person_code, tax_year):
        self.l = LogHelper("HMRC")
        self.l.set_level_debug()
        self.l.debug(__file__)

        self.person_code = person_code
        self.tax_year = tax_year
        self.constants = HMRC_ConstantsByYear(tax_year)

        self.person = HMRC_People(person_code)

        spouse_code = self.person.get_spouse_code()

        self.spouse = HMRC_People(spouse_code)

        self.categories = Categories()
        self.transactions = Transactions()

        self.sql = SQL_Helper().select_sql_helper("SQLite")

    def are_you_liable_to_pension_savings_tax_charges(self):
        return False

    def call_method(self, method_name):
        self.l.debug(f"Calling method: {method_name}")
        try:
            method = getattr(self, method_name)
            return method()
        except AttributeError:
            self.l.error(f'\tdef {method_name}(self): return "Undefined"')

    def did_property_rental_income_cease(self):
        return False

    def did_you_get_dividend_income(self):
        person_code = self.person_code
        tax_year = self.tax_year

        category_like = f"HMRC {person_code} DIV income: "

        total = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return total > 0

    def did_you_get_eea_furnished_holiday_lettings_income(self):
        return False

    def did_you_get_income_from_property_let_jointly(self):
        return False

    def did_you_get_uk_furnished_holiday_lettings_income(self):
        return False

    def get_answers(self):
        questions = self.get_questions()

        answers = []
        for question, section, header, box, method_name, information in questions:
            answer = self.call_method(method_name)

            answers.append([question, section, header, box, answer, information])

        return answers

    def get_any_other_information(self):
        return False

    def get_balancing_charges_gbp(self):
        return uf.format_as_gbp(0)

    def get_property_allowance_gbp(self):
        property_allowance = self.get_property_allowance()
        return uf.format_as_gbp(property_allowance)

    def get_savings_allowance_gbp(self):
        savings_allowance = self.get_savings_allowance()
        return uf.format_as_gbp(savings_allowance)

    def get_rent__rates__insurance_and_ground_rents_gbp(self):
        return uf.format_as_gbp(self.get_rent__rates__insurance_and_ground_rents())

    def get_property_repairs_and_maintenance_gbp(self):
        return uf.format_as_gbp(self.get_property_repairs_and_maintenance())

    def get_non_residential_finance_property_costs_gbp(self):
        return uf.format_as_gbp(0)

    def get_legal__management_and_other_professional_fees_gbp(self):
        return uf.format_as_gbp(
            self.get_legal__management_and_other_professional_fees()
        )

    def get_costs_of_services_provided__including_wages_gbp(self):
        return uf.format_as_gbp(self.get_costs_of_services_provided__including_wages())

    def get_other_information_about_this_business(self):
        return ""

    def get_other_information_about_your_uk_property_income(self):
        return ""

    def do_you_need__additional_information__pages_tr(self):
        return ""

    def get_other_property_expenses_gbp(self):
        return uf.format_as_gbp(self.get_other_property_expenses())

    def get_total_property_expenses_gbp(self):
        return uf.format_as_gbp(self.get_total_property_expenses())

    def get_blind_person_s_surplus_allowance_you_can_have(self):
        return "Not applicable"

    def get_total_income_gbp(self):
        return uf.format_as_gbp(self.get_total_income())

    def get_marriage_allowance_transfer_amount(self):
        if self.get_marital_status() != "Married":
            return 0

        total_income = self.get_total_income()

        spouse_total_income = self.get_spouse_total_income()

        if total_income > spouse_total_income:
            return 0

        marriage_allowance = self.constants.get_marriage_allowance()

        personal_allowance = self.constants.get_personal_allowance()

        total_income_excluding_tax_free_savings = (
            self.get_total_income_excluding_tax_free_savings()
        )

        if total_income_excluding_tax_free_savings > personal_allowance:
            return 0

        return min(
            marriage_allowance,
            personal_allowance - total_income_excluding_tax_free_savings,
        )

    def get_marriage_allowance_transfer_amount_gbp(self):
        return uf.format_as_gbp(self.get_marriage_allowance_transfer_amount())

    def are_you_claiming_marriage_allowance(self):
        if self.get_marital_status() != "Married":
            return False

        total_income = self.get_total_income()

        spouse_total_income = self.get_spouse_total_income()

        if total_income > spouse_total_income:
            return False

        personal_allowance = self.constants.get_personal_allowance()

        total_income_excluding_tax_free_savings = (
            self.get_total_income_excluding_tax_free_savings()
        )

        if total_income_excluding_tax_free_savings > personal_allowance:
            return False

        return True

    def get_class_2_nics_weekly_rate(self):
        return self.constants.get_class_2_nics_weekly_rate()

    def get_small_profits_threshold(self):
        return self.constants.get_small_profits_threshold()

    def get_class_2_nics_amount_gbp(self):
        how_many_weeks_in_an_hmrc_year = 52
        class_2_nics_weekly_rate = self.get_class_2_nics_weekly_rate()
        return how_many_weeks_in_an_hmrc_year * class_2_nics_weekly_rate

    def do_you_want_to_pay_class_2_nics_voluntarily(self):
        taxable_profits = self.get_total_taxable_profits_from_this_business()
        small_profits_threshold = self.get_small_profits_threshold()

        return taxable_profits < small_profits_threshold

    def get_class_2_nics_due(self):
        return "Not applicable"

    def do_you_want_to_claim_rent_a_room_relief(self):
        return False

    def get_how_many_properties_do_you_rent_out(self):
        # search the transactions table for any records in this tax year
        # which have a property income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} UKP income%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many

    def get_class_4_nics_due(self):
        return "Not applicable"

    def get_first_name(self):
        return self.person.get_first_name()

    def get_last_name(self):
        return self.person.get_last_name()

    def get_middle_name(self):
        return self.person.get_middle_name()

    def get_postgraduate_loan_repayment_due(self):
        return "Not applicable"

    def get_student_loan_repayment_due(self):
        return "Not applicable"

    def get_total_tax_due(self):
        return "Not applicable"

    def get_total_tax_overpaid(self):
        return "Not applicable"

    def get_capital_gains_tax_due(self):
        return "Not applicable"

    def get_first_payment_on_account_for_next_year(self):
        return "Not applicable"

    def get_pension_charges_due(self):
        return "Not applicable"

    def reduce_next_year_payments_on_account(self):
        return "Not applicable"

    def get_underpaid_tax(self):
        return "Not applicable"

    def get_underpaid_tax_for_earlier_years(self):
        return "Not applicable"

    def get_married_people_s_surplus_allowance_you_can_have(self):
        return "Not applicable"

    def is_total_property_income_more_than_property_allowance(self):
        property_income_allowance = self.get_property_income_allowance()

        property_income = self.get_property_income()

        gbp_income = uf.format_as_gbp(property_income)
        gbp_allowance = uf.format_as_gbp(property_income_allowance)

        if property_income > property_income_allowance:
            return f"Yes: Income {gbp_income} > {gbp_allowance} Property allowance"
        else:
            return f"No: Income {gbp_income} <= {gbp_allowance} Allowance"

    def is_total_trading_income_more_than_trading_allowance(self):
        trading_allowance = self.get_trading_allowance()
        trading_income = self.get_trading_income()

        return trading_income > trading_allowance

    def is_property_allowance_more_than_property_expenses(self):
        property_allowance = self.get_property_allowance()
        property_expenses = self.get_property_expenses()

        return property_allowance > property_expenses

    def is_property_income_more_than_property_allowance(self):
        property_allowance = self.get_property_allowance()
        property_income = self.get_property_income()

        return property_income > property_allowance

    def is_trading_allowance_more_than_trading_expenses(self):
        trading_allowance = self.get_trading_allowance()
        trading_expenses = self.get_trading_expenses()

        return trading_allowance > trading_expenses

    def is_trading_income_more_than_trading_allowance(self):
        trading_allowance = self.get_trading_allowance()
        trading_income = self.get_trading_income()

        return trading_income > trading_allowance

    def did_you_get_pensions__annuities__or_state_benefits(self):

        total = self.get_pensions() + self.get_state_benefits()

        return total > 0

    def get_pensions(self):
        person_code = self.person_code
        tax_year = self.tax_year

        category_like = f"HMRC {person_code} PEN income: "

        return self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

    def get_state_benefits(self):
        person_code = self.person_code
        tax_year = self.tax_year

        category_like = f"HMRC {person_code} BEN income: "

        return self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

    def get_how_many_businesses(self):
        hmrc_businesses = self.get_hmrc_businesses()

        return len(hmrc_businesses)

    def get_business_name(self):
        if self.get_how_many_businesses() > 0:
            hmrc_businesses = self.get_hmrc_businesses()

            return hmrc_businesses[0].get_business_name()
        else:
            return "Not applicable"

    def get_hmrc_businesses(self):
        hmrc_businesses = []
        # search the transactions table for any records in this tax year
        # which have a self-employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year

        category_like = f"HMRC {person_code} SES income: "
        where = f'"Tax year"="{tax_year}" AND "Category" LIKE "{category_like}%"'

        query = (
            self.transactions.query_builder()
            .select_raw("DISTINCT Category")
            .where(where)
            .build()
        )

        rows = self.sql.fetch_all(query)

        start_position = len(category_like)

        for row in rows:
            business_name = row[0][start_position:]
            hmrc_business = HMRC_Businesses(business_name)
            hmrc_businesses.append(hmrc_business)

        return hmrc_businesses

    def were_you_in_partnership_s__this_tax_year(self):
        return False

    def did_you_get_uk_interest(self):
        taxed_uk_interest = self.get_taxed_uk_interest()

        untaxed_uk_interest = self.get_untaxed_uk_interest()

        total_interest = taxed_uk_interest + untaxed_uk_interest

        return total_interest > 0

    def did_you_get_child_benefit(self):
        return False

    def get_decrease_in_tax_due_to_adjustments_to_an_earlier_year(self):
        return "Not applicable"

    def get_increase_in_tax_due_to_adjustments_to_an_earlier_year(self):
        return "Not applicable"

    def get_any_repayments_claimed_for_next_year(self):
        return "Not applicable"

    def get_tc_please_give_any_other_information_in_this_space(self):
        return ""

    def get_tr_please_give_any_other_information_in_this_space(self):
        return ""

    def get_additional_information(self):
        return "Maybe: Married couples allowance section"
        # return False

    def get_number_of_properties_rented_out(self):
        return "Not applicable"

    def ceased_renting__consider_cgt(self):
        return "Not applicable"

    def is_any_property_let_jointly(self):
        return "Not applicable"

    def claim_rent_a_room_relief(self):
        return "Not applicable"

    def get_total_rents_and_other_income_from_property_gbp(self):
        return self.get_property_income()

    def get_total_rents_and_other_income_from_property(self):
        return None

    def did_you_use_traditional_accounting(self):
        return False

    def get_uk_tax_taken_off_total_rents_gbp(self):
        return uf.format_as_gbp(0)

    def get_premiums_for_the_grant_of_a_lease_gbp(self):
        return uf.format_as_gbp(0)

    def get_reverse_premiums_and_inducements_gbp(self):
        return uf.format_as_gbp(0)

    def get_total_uk_property_income_gbp(self):
        return self.get_property_income()

    def get_personal_allowance(self):
        return self.constants.get_personal_allowance()

    def did_you_use_cash_basis(self):
        return True

    def get_tax_taken_off_any_income_in_box_20(self):
        return "Not applicable"

    def get_premiums_for_the_grant_of_a_lease(self):
        return "Not applicable"

    def get_reverse_premiums(self):
        return "Not applicable"

    def get_rent__rates__insurance_and_ground_rents(self) -> float:
        category_like = "UKP expense: rent, rates"

        rent_rates_etc = self.get_total_transactions_by_category_like(category_like)

        return rent_rates_etc

    def get_property_repairs_and_maintenance(self) -> float:
        category_like = "UKP expense: repairs and maintenance"

        repairs_and_maintenance = self.get_total_transactions_by_category_like(
            category_like
        )

        return repairs_and_maintenance

    def get_total_transactions_by_category_like(self, category_like) -> float:
        person_code = self.person_code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} {category_like}"

        total = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return total

    def get_non_residential_finance_property_costs(self):
        return "Not applicable"

    def get_legal__management_and_other_professional_fees(self) -> float:
        category_like = "UKP expense: legal"

        legal__management_and_other_professional_fees = (
            self.get_total_transactions_by_category_like(category_like)
        )

        return legal__management_and_other_professional_fees

    def get_total_property_expenses(self) -> float:
        category_like = "UKP expense: "

        total_property_expenses = self.get_total_transactions_by_category_like(
            category_like
        )

        return total_property_expenses

    def get_costs_of_services_provided__including_wages(self):
        return 0

    def get_other_property_expenses(self):
        return 0

    def get_private_use_adjustment_gbp(self):
        return uf.format_as_gbp(0)

    def get_electric_charge_point_allowance_gbp(self):
        return uf.format_as_gbp(0)

    def get_freeport_allowance_gbp(self):
        return uf.format_as_gbp(0)

    def get_zero_emission_goods_vehicle_allowance_gbp(self):
        return uf.format_as_gbp(0)

    def get_all_other_capital_allowances_gbp(self):
        return uf.format_as_gbp(0)

    def get_adjusted_profit_for_the_year_gbp(self):
        return "Undefined"

    def get_loss_brought_forward_against_this_year_s_profits_gbp(self):
        return "Undefined"

    def get_taxable_profit_for_the_year_gbp(self):
        return "Undefined"

    def get_adjusted_loss_for_the_year_gbp(self):
        return "Undefined"

    def get_loss_to_carry_forward__inc_unused_losses_gbp(self):
        return "Undefined"

    def get_residential_property_finance_costs_gbp(self):
        return "Undefined"

    def get_unused_residential_finance_costs_brought_forward_gbp(self):
        return "Undefined"

    def get_any_other_information_about_your_uk_property_income(self):
        return "Undefined"

    def get_rental_income_gbp(self):
        return "Undefined"

    def get_total_income_excluding_tax_free_savings(self):
        total_income = self.get_total_income()
        savings_income = self.get_savings_income()

        return total_income - savings_income

    def get_total_income__excluding_tax_free_savings__gbp(self):
        trading_income_gbp = self.get_trading_income__turnover__gbp()
        property_income_gbp = self.get_property_income_gbp()
        t_and_p_gbp = uf.format_as_gbp(
            self.get_total_income_excluding_tax_free_savings()
        )
        return f"{t_and_p_gbp} = {trading_income_gbp} (trading) {property_income_gbp} (property)"

    def get_adjustments_gbp(self):
        return "Undefined"

    def get_adjusted_profit_or_loss_for_the_year_gbp(self):
        return "Undefined"

    def get_losses_brought_forward_and_set_off_gbp(self):
        return "Undefined"

    def get_taxed_uk_interest_after_tax_has_been_taken_off_gbp(self):
        return "Undefined"

    def get_untaxed_uk_interest_gbp(self):
        return "Undefined"

    def get_untaxed_foreign_interest__up_to__2_000__gbp(self):
        return "Undefined"

    def get_relief_at_source_pension_payments_to_ppr_gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_payments_to_pension_schemes__relief_at_source()
        )

    def get_total_of_one_off_payments_gbp(self):
        return self.get_relief_at_source_pension_payments_to_ppr_gbp()

    def get_payments_to_a_retirement_annuity_contract(self):
        return 0

    def get_payments_to_a_retirement_annuity_contract_gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_payments_to_a_retirement_annuity_contract()
        )

    def get_payments_to_your_employer_s_scheme(self):
        return 0

    def get_payments_to_your_employer_s_scheme_gbp(self):
        return uf.format_as_gbp_or_blank(self.get_payments_to_your_employer_s_scheme())

    def get_payments_to_an_overseas_pension_scheme(self):
        return 0

    def get_payments_to_an_overseas_pension_scheme_gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_payments_to_an_overseas_pension_scheme()
        )

    def get_amount_of_underpaid_tax_for_earlier_years__paye__gbp(self):
        return uf.format_as_gbp(0)

    def get_estimated_underpaid_tax_for_this_tax_year_paye_gbp(self):
        return uf.format_as_gbp(0)

    def get_outstanding_debt_included_in_tax_code(self):
        return 0

    def get_outstanding_debt_included_in_tax_code_gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_outstanding_debt_included_in_tax_code()
        )

    def get_increase_in_tax_due_to_earlier_years_adjustments(self):
        return 0

    def get_increase_in_tax_due_to_earlier_years_adjustments_gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_increase_in_tax_due_to_earlier_years_adjustments()
        )

    def get_decrease_in_tax_due_to_earlier_years_adjustments(self):
        return 0

    def get_decrease_in_tax_due_to_earlier_years_adjustments_gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_decrease_in_tax_due_to_earlier_years_adjustments()
        )

    def get_any_next_year_repayment_you_are_claiming_now(self):
        return 0

    def get_any_next_year_repayment_you_are_claiming_now_gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_any_next_year_repayment_you_are_claiming_now()
        )

    def does_this_return_contain_provisional_figures(self):
        return False

    def do_you_want_to_add_an_attachment_to_the_return(self):
        return False

    def get_cost_to_replace_residential_domestic_items_gbp(self):
        return "Undefined"

    def get_private_use_adjustment(self):
        return "Not applicable"

    def get_balancing_charges(self):
        return "Not applicable"

    def get_structures_and_buildings_allowance(self):
        return "Not applicable"

    def get_electric_charge_point_allowance(self):
        return "Not applicable"

    def get_freeport_allowance(self):
        return "Not applicable"

    def get_zero_emissions_allowance(self):
        return "Not applicable"

    def get_all_other_capital_allowances(self):
        return "Not applicable"

    def get_costs_of_replacing_domestic_items(self):
        return "Not applicable"

    def get_rent_a_room_exempt_amount(self):
        return "Not applicable"

    def get_adjusted_profit_for_the_year(self):
        return "Not applicable"

    def get_taxable_profit_for_the_year(self):
        return "Not applicable"

    def get_adjusted_loss_for_the_year(self):
        return "Not applicable"

    def get_loss_set_off_against_income(self):
        return "Not applicable"

    def get_loss_to_carry_forward(self):
        return "Not applicable"

    def get_residential_property_finance_costs(self):
        return "Not applicable"

    def get_unused_residential_finance_costs_brought_forward(self):
        return "Not applicable"

    def get_any_tax_taken_off_box_17(self):
        return 0

    def get_benefit_from_pre_owned_assets(self):
        return 0

    def do_you_need_to_complete_the_capital_gains_section(self):
        return False

    def are_computations_provided(self):
        return False

    def get_description_of_income_in_boxes_17_and_20(self):
        return ""

    def get_dividends_from_uk_companies(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Dividends from UK companies"
        )

    def get_foreign_dividends(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Foreign dividends"
        )

    def did_you_get_any_foreign_income(self):
        return False

    def get_full_utr(self) -> str:
        utr: str = self.person.get_unique_tax_reference()
        utr_check_digit: str = self.person.get_utr_check_digit()
        return utr + utr_check_digit

    def get_unique_taxpayer_reference__utr_(self):
        return self.person.get_unique_tax_reference()

    def get_email_address(self):
        return self.person.get_email_address()

    def get_marital_status(self):
        return self.person.get_marital_status()

    def are_you_registered_blind(self):
        return False

    def get_how_many_self_employed_businesses_did_you_have(self):
        # search the transactions table for any records in this tax year
        # which have a self-employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} SES income%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many

    def get_how_many_employments(self):
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} EMP%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many

    def get_lump_sum_pension___available_lifetime_allowance(self):
        return "Not applicable"

    def get_non_lump_sum_pension___available_lifetime_allowance(self):
        return "Not applicable"

    def get_lifetime_allowance_tax_paid_by_your_pension_scheme(self):
        return "Not applicable"

    def get_amount_saved_to_pension___available_lifetime_allowance(self):
        return "Not applicable"

    def get_annual_allowance_tax_paid(self):
        return "Not applicable"

    def get_amount_subject_to_overseas_transfer_charge(self):
        return "Not applicable"

    def get_tax_paid_on_overseas_transfer_charge(self):
        return "Not applicable"

    def get_pension_scheme_tax_reference_number(self):
        return "Not applicable"

    def get_unauthorised_pension_payment_not_surcharged_(self):
        return "Not applicable"

    def get_unauthorised_pension_payment_surcharged_(self):
        return "Not applicable"

    def get_foreign_tax_paid_on_an_unauthorised_payment(self):
        return "Not applicable"

    def get_taxable_short_service_refund__overseas_only_(self):
        return "Not applicable"

    def get_box_17_is_not_in_use(self):
        return "Not applicable"

    def get_foreign_tax_paid_on_box_16(self):
        return "Not applicable"

    def get_tax_avoidance_scheme_reference_number(self):
        return "Not applicable"

    def get_tax_year_expected_advantage_arises(self):
        return "Not applicable"

    def get_business_description(self):
        if self.get_how_many_businesses() > 0:
            business_name = self.get_business_name()
            hmrc_business = HMRC_Businesses(business_name)
            business_description = hmrc_business.get_business_description()

            return business_description
        else:
            return ""

    def get_business_postcode(self):
        if self.get_how_many_businesses() > 0:
            business_name = self.get_business_name()
            hmrc_business = HMRC_Businesses(business_name)
            business_postcode = hmrc_business.get_business_postcode()

            return business_postcode
        else:
            return ""

    def have_business_details_changed(self):
        return False

    def are_you_a_foster_carer(self):
        return False

    def get_business_start_date__in_this_tax_year_(self):
        return "Not applicable"

    def get_business_end_date__in_this_tax_year_(self):
        return "Not applicable"

    def get_date_the_books_are_made_up_to(self):
        end_year = self.tax_year[-4:]
        return f"05/04/{end_year}"

    def get_property_income(self) -> float:
        person_code = self.person_code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} UKP income"

        property_income = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return property_income

    def get_savings_income(self) -> float:
        person_code = self.person_code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} INT income"

        savings_income = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return savings_income

    def get_spouse_total_income(self) -> float:
        person_code = self.spouse.code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} % income"

        total_income = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return total_income

    def get_total_income(self) -> float:
        person_code = self.person_code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} % income"

        total_income = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return total_income

    def get_property_income_gbp(self) -> str:
        return uf.format_as_gbp(self.get_property_income())

    def get_savings_income_gbp(self) -> str:
        return uf.format_as_gbp(self.get_savings_income())

    def get_trading_income__turnover__gbp(self) -> str:
        return uf.format_as_gbp(self.get_trading_income())

    def get_trading_income(self) -> float:
        if self.get_how_many_self_employed_businesses_did_you_have() > 1:
            raise ValueError("More than one business. Review the code")

        person_code = self.person_code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} SES income"

        trading_income = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return trading_income

    def __get_breakdown(self, category_like):
        # search the transactions table for any records in this tax year
        # which have an appropriate category for the current person
        tax_year = self.tax_year

        query = (
            self.transactions.query_builder()
            .select("Date", "Key", "Description", "Note", "Nett", "Category")
            .where(f'"Tax year"="{tax_year}" AND "Category" LIKE "{category_like}%"')
            .order("Date")
            .build()
        )
        self.l.debug(query)
        rows = self.sql.fetch_all(query)  # Fetch all rows from the database
        if not rows:
            return ""  # Return an empty string if no rows are fetched

        # Widths assume output printed is Courier New size 10 in landscape

        max_description_width = 40
        max_category_width = max_description_width

        # Use a list for efficient concatenation
        breakdown = ["Date | Account | Description | Note | Nett | Category"]
        for row in rows:
            breakdown.append(
                f"{row[0]} | {row[1]} | {row[2][:max_description_width]} | {row[3]} | {row[4]:>10.2f} | {row[5][:max_category_width]}"
            )

        return self.format_breakdown(breakdown)

    def format_breakdown(self, breakdown) -> str:
        # Split each line into fields by the '|' delimiter
        fields = [line.split("|") for line in breakdown]

        # Determine the maximum width of each column
        max_widths = [max(len(field.strip()) for field in col) for col in zip(*fields)]

        # Format each line by aligning fields to their respective column widths
        formatted_lines = [
            " | ".join(
                field.strip().ljust(width) if index != 4 else field.strip().rjust(width)
                for index, (field, width) in enumerate(zip(line, max_widths))
            )
            for line in fields
        ]

        # Join all formatted lines with newlines
        return "\n" + "\n".join(formatted_lines)

    def get_property_expenses_breakdown(self):
        # search the transactions table for any records in this tax year
        # which have a property expense category for the current person
        person_code = self.person_code
        category_like = f"HMRC {person_code} UKP expense"

        return self.__get_breakdown(category_like)

    def get_property_income_breakdown(self):
        # search the transactions table for any records in this tax year
        # which have a property income category for the current person
        person_code = self.person_code
        category_like = f"HMRC {person_code} UKP income"

        return self.__get_breakdown(category_like)

    def get_savings_income_breakdown(self):
        # search the transactions table for any records in this tax year
        # which have a savings income category for the current person
        person_code = self.person_code
        category_like = f"HMRC {person_code} INT income"

        return self.__get_breakdown(category_like)

    def get_trading_expenses_breakdown(self):
        # search the transactions table for any records in this tax year
        # which have a self-employment expense category for the current person
        person_code = self.person_code
        category_like = f"HMRC {person_code} SES expense"

        return self.__get_breakdown(category_like)

    def get_trading_income_breakdown(self):
        # search the transactions table for any records in this tax year
        # which have a self-employment income category for the current person
        person_code = self.person_code
        category_like = f"HMRC {person_code} SES income"

        return self.__get_breakdown(category_like)

    def get_other_business_income_not_included_as_trading_income(self):
        return 0

    def get_other_business_income_not_trading_income_gbp(self):
        return uf.format_as_gbp(
            self.get_other_business_income_not_included_as_trading_income()
        )

    def get_business_income(self):
        return (
            self.get_trading_income()
            + self.get_other_business_income_not_included_as_trading_income()
        )

    def get_business_income_gbp(self):
        return uf.format_as_gbp(self.get_business_income())

    def get_how_would_you_like_to_record_your_expenses(self):
        return "As a single total value"

    def get_taxpayer_residency_status(self):
        return self.person.get_taxpayer_residency_status()

    def get_trading_expenses_gbp(self):
        return uf.format_as_gbp(self.get_trading_expenses())

    def get_trading_expenses_gbpX(self):
        if self.use_trading_allowance:
            return uf.format_as_gbp(0)
        else:
            return uf.format_as_gbp(self.get_trading_expenses())

    def get_trading_allowance_gbp(self):
        trading_allowance = self.get_trading_allowance()
        return uf.format_as_gbp(trading_allowance)

    def get_claimed_property_allowance_gbp(self):
        self.l.debug("get_claimed_property_allowance")
        if self.use_property_allowance():
            property_allowance = self.get_property_allowance()
            return uf.format_as_gbp(property_allowance)
        else:
            return uf.format_as_gbp_or_blank(0)

    def get_claimed_trading_allowance_gbp(self):
        if self.use_trading_allowance():
            trading_allowance = self.get_trading_allowance()
            return uf.format_as_gbp(trading_allowance)
        else:
            return uf.format_as_gbp_or_blank(0)

    def get_property_allowance(self):
        return self.constants.get_property_income_allowance()

    def get_savings_allowance(self):
        return self.constants.get_personal_savings_allowance()

    def get_trading_allowance(self):
        return self.constants.get_trading_income_allowance()

    def use_property_allowance(self):
        self.l.debug("use_property_allowance")
        property_allowance = self.get_property_allowance()
        self.l.debug(property_allowance)
        property_expenses = self.get_property_expenses()
        self.l.debug(property_expenses)

        return property_allowance > property_expenses

    def use_trading_allowance(self):
        trading_allowance = self.get_trading_allowance()
        trading_expenses = self.get_trading_expenses()

        return trading_allowance > trading_expenses

    def get_trading_income_was_below__85k__total_expenses_in_box_20(self):
        return "See box 20"

    def get_property_expenses(self):
        self.l.debug("get_property_expenses")
        person_code = self.person_code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} UKP expense"

        property_expenses = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )
        self.l.debug(property_expenses)

        return property_expenses

    def get_property_expenses_gbp(self):
        return uf.format_as_gbp(self.get_property_expenses())

    def get_trading_expenses(self):
        if self.get_how_many_self_employed_businesses_did_you_have() > 1:
            raise ValueError("More than one business. Review the code")

        person_code = self.person_code
        tax_year = self.tax_year
        category_like = f"HMRC {person_code} SES expense"

        trading_expenses = self.transactions.fetch_total_by_tax_year_category_like(
            tax_year, category_like
        )

        return trading_expenses

    def get_bottom_line(self):
        return self.get_business_income() - self.get_trading_expenses()

    def get_bottom_line_gbp(self):
        return uf.format_as_gbp(self.bottom_line())

    def get_net_loss(self):
        return min(0, self.get_bottom_line()) * -1

    def get_net_loss_gbp(self):
        return uf.format_as_gbp(self.get_net_loss())

    def get_net_profit(self):
        return max(0, self.get_bottom_line())

    def get_net_profit_gbp(self):
        return uf.format_as_gbp(self.get_net_profit())

    def get_annual_investment_allowance_gbp(self):
        return ""

    def get_small_balance_unrelieved_expenditure_allowance_gbp(self):
        return ""

    def get_zero_emission_car_allowance_gbp(self):
        return ""

    def get_other_capital_allowances_gbp(self):
        return ""

    def get_structures_and_buildings_allowance_gbp(self):
        return ""

    def get_profit_or_loss_gbp(self):
        profit = self.get_profit()
        if profit > 0:
            return self.get_profit_gbp()
        else:
            return self.get_loss_gbp()

    def get_capital_allowances_gbp(self):
        return uf.format_as_gbp(0)

    def get_tax_adjustments_gbp(self):
        return uf.format_as_gbp(0)

    def get_taxable_profits_or_net_loss__before_set_offs__gbp(self):
        return uf.format_as_gbp(self.get_net_business_profit_for_tax_purposes())

    def get_freeport_and_investment_zones_allowance_gbp(self):
        return ""

    def get_total_balancing_charges_gbp(self):
        return ""

    def get_goods_or_services_for_your_own_use_gbp(self):
        return ""

    def get_net_business_profit_for_tax_purposes(self):
        income = self.get_business_income()
        if self.use_trading_allowance():
            net_business_profit_for_tax_purposes = max(
                0, income - self.get_trading_allowance()
            )
        else:
            net_business_profit_for_tax_purposes = max(
                0, income - self.get_trading_expenses()
            )

        return net_business_profit_for_tax_purposes

    def get_net_business_profit_for_tax_purposes_gbp(self):
        return uf.format_as_gbp(self.get_net_business_profit_for_tax_purposes())

    def get_loss_brought_forward_set_off_against_profits(self):
        return 0

    def get_loss_brought_forward_set_off_against_profits_gbp(self):
        return uf.format_as_gbp(self.get_loss_brought_forward_set_off_against_profits())

    def get_other_business_income_not_already_included(self):
        return 0

    def get_other_business_income_not_already_included_gbp(self):
        return uf.format_as_gbp(self.get_other_business_income_not_already_included())

    def get_total_taxable_profits_from_this_business(self):
        net_business_profit_for_tax_purposes = (
            self.get_net_business_profit_for_tax_purposes()
        )

        other_business_income_not_already_included = (
            self.get_other_business_income_not_already_included()
        )

        loss_brought_forward_set_off_against_profits = (
            self.get_loss_brought_forward_set_off_against_profits()
        )

        total_taxable_profits_from_this_business = (
            net_business_profit_for_tax_purposes
            + other_business_income_not_already_included
            - loss_brought_forward_set_off_against_profits
        )

        return total_taxable_profits_from_this_business

    def get_total_taxable_profits_from_this_business_gbp(self):
        return uf.format_as_gbp(self.get_total_taxable_profits_from_this_business())

    def get_net_business_loss_for_tax_purposes(self):
        income = self.get_business_income()
        net_business_loss_for_tax_purposes = (
            min(0, income - self.get_trading_expenses()) * -1
        )

        return net_business_loss_for_tax_purposes

    def get_net_business_loss_for_tax_purposes_gbp(self):
        return uf.format_as_gbp(self.get_net_business_loss_for_tax_purposes())

    def get_loss_set_off_against_other_income_this_tax_year(self):
        return 0

    def get_loss_set_off_against_other_income_this_tax_year_gbp(self):
        return uf.format_as_gbp(
            self.get_loss_set_off_against_other_income_this_tax_year()
        )

    def get_loss_carried_back_prior_years_set_off_income_cg(self):
        return 0

    def get_loss_carried_back_prior_years_set_off_income_cg_gbp(self):
        return uf.format_as_gbp(
            self.get_loss_carried_back_prior_years_set_off_income_cg()
        )

    def get_loss_to_take_forward_post_set_offs_unused_losses(self):
        return 0

    def get_loss_to_take_forward_post_set_offs_unused_losses_gbp(self):
        return uf.format_as_gbp(
            self.get_loss_to_take_forward_post_set_offs_unused_losses()
        )

    def get_construction_industry_deductions_gbp(self):
        return False

    def were_you_over_state_pension_age_at_tax_year_start(self):
        return False

    def were_you_under_16_at_tax_year_start(self):
        return False

    def were_you_not_resident_in_uk_during_the_tax_year(self):
        return False

    def are_you_a_trustee__executor_or_administrator(self):
        return False

    def are_you_a_diver(self):
        return False

    def get_please_give_any_other_information_about_this_business(self):
        return ""

    def are_total_profits____6_725_voluntary_class_2_nics(self):
        return "Not applicable"

    def are_you_exempt_from_paying_class_4_nics(self):
        return "Not applicable"

    def get_total_construction_industry_scheme__cis__deductions(self):
        return "Not applicable"

    def get_how_many_partnerships(self):
        return 0

    def get_jobseeker_s_allowance(self):
        return 0

    def any_more_pages(self):
        return False

    def get_other_dividends(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INC Other dividends"
        )

    def did_you_get_other_taxable_income(self):
        return False

    def did_you_make_pension_contributions(self):
        pension_contributions = self.get_pension_contributions()
        return pension_contributions > 0

    def get_pension_contributions(self):
        person_code = self.person_code
        pension_contributions = self.transactions.fetch_total_by_tax_year_category(
            self.tax_year, f"HMRC {person_code} RLF pension contribution"
        )
        return pension_contributions

    def get_payments_to_pension_schemes__relief_at_source(self):
        person_code = self.person_code
        payments_to_pension_schemes = (
            self.transactions.fetch_total_by_tax_year_category_like(
                self.tax_year, f"HMRC {person_code} RLF pension"
            )
        )
        return payments_to_pension_schemes

    def get_payments_to_pension_schemes__relief_at_source__gbp(self):
        return uf.format_as_gbp_or_blank(
            self.get_payments_to_pension_schemes__relief_at_source()
        )

    def get_pensions__other_than_state_pension_(self):
        return 0

    def residence__remittance_basis_etc(self):
        return False

    def get_questions(self):
        if self.report_type == HMRC.ONLINE_REPORT:
            return HMRC_QuestionsByYear(self.tax_year).get_online_questions()
        else:
            return HMRC_QuestionsByYear(self.tax_year).get_printed_form_questions()

    def get_spouse_code(self):
        return self.person.get_spouse_code()

    def get_state_pension(self):
        return 0

    def get_state_pension_lump_sum(self):
        return 0

    def get_tax_taken_off_box_9(self):
        return 0

    def get_tax_taken_off_box_11(self):
        return 0

    def get_tax_taken_off_foreign_dividends(self):
        return 0

    def get_tax_taken_off_incapacity_benefit_in_box_13(self):
        return 0

    def get_taxable_incapacity_benefit(self):
        return 0

    def get_taxed_uk_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INT income: interest UK taxed"
        )

    def get_payments_to_annuity_tax_relief_not_claimed(self):
        return 0

    def get_payments_to_employers_scheme_where_no_tax_deducted(self):
        return 0

    def get_payments_to_overseas_pension_scheme(self):
        return 0

    def get_gift_aid_payments(self):
        return "Not applicable"

    def get_total_of_any__one_off__payments_in_box_5(self):
        return "Not applicable"

    def get_gift_aid_payments_from_previous_tax_year_(self):
        return "Not applicable"

    def get_gift_aid_payments_after_end_of_tax_year(self):
        return "Not applicable"

    def get_value_of_shares_dividends_gifted_to_charities(self):
        return "Not applicable"

    def get_value_of_land_or_buildings_gifted_to_charities(self):
        return "Not applicable"

    def get_value_gifted_to_non_uk_charities_in_box_9_and_10(self):
        return "Not applicable"

    def get_for_how_many_children__cb_(self):
        return "Not applicable"

    def get_date_cb_stopped(self):
        return "Not applicable"

    def get_your_spouse_s_first_name(self):
        return self.spouse.get_first_name()

    def get_your_spouse_s_last_name(self):
        return self.spouse.get_last_name()

    def get_your_spouse_s_national_insurance_number(self):
        return self.spouse.get_national_insurance_number()

    def get_your_spouse_s_date_of_birth(self):
        return self.spouse.get_uk_date_of_birth()

    def get_marriage_date(self):
        return self.spouse.get_uk_marriage_date()

    def get_refunded_or_off_set_income_tax(self):
        return "Not applicable"

    def use_paye_for_small_amount_payments(self):
        return "No"

    def use_paye_for_tax_on_savings(self):
        return "No"

    def get_bank_name(self):
        return self.person.get_bank_name()

    def get_bank_account_holder(self):
        return self.person.get_name()

    def get_branch_sort_code(self):
        return self.person.get_branch_sort_code()

    def get_bank_account_number(self):
        return self.person.get_bank_account_number()

    def get_building_society_reference_number(self):
        return "Not applicable"

    def cheque(self):
        return "No"

    def did_you_put_a_nominee_s_name_in_box_5(self):
        return "No"

    def is_your_nominee_your_tax_advisor(self):
        return "Not applicable"

    def get_nominee_s_address(self):
        return "Not applicable"

    def get_nominee_s_postcode(self):
        return "Not applicable"

    def get_signature_to_authorise_nominee(self):
        return "Not applicable"

    def get_tax_advisor_s_name(self):
        return "Not applicable"

    def get_tax_advisor_s_phone_number(self):
        return "Not applicable"

    def get_tax_advisor_s_address_and_postcode(self):
        return "Not applicable"

    def get_tax_advisor_s_reference(self):
        return "Not applicable"

    def are_figures_provisional(self):
        return False

    def are_supplementary_pages_enclodsed(self):
        return "Not applicable"

    def get_declaration_signature(self):
        return "Not applicable"

    def get_declaration_date(self):
        return "Not applicable"

    def get_signing_capacity_if_signing_for_someone_else(self):
        return "Not applicable"

    def get_name_of_the_peson_you_ve_signed_for(self):
        return "Not applicable"

    def get_if_you_filled_in_boxes_23_and_24_enter_your_name(self):
        return "Not applicable"

    def get_your_address(self):
        return self.person.get_address()

    def get_gilt_interest_after_tax_taken_off(self):
        return "Not applicable"

    def get_tax_taken_off(self):
        return "Not applicable"

    def get_gross_amount_before_tax(self):
        return "Not applicable"

    def get_uk_gains_where_tax_was_treated_as_paid(self):
        return "Not applicable"

    def get_number_of_years_policy_was_last_held_or_received_gain(self):
        return "Not applicable"

    def get_uk_gains_where_tax_was_not_treated_as_paid(self):
        return "Not applicable"

    def get_how_many_years_policy_was_last_held_or_received_gain(self):
        return "Not applicable"

    def get_gains_from_voided_isas(self):
        return "Not applicable"

    def get_years_voided_isas_held(self):
        return "Not applicable"

    def get_tax_taken_off_gain_in_box_8(self):
        return "Not applicable"

    def get_deficiency_relief(self):
        return "Not applicable"

    def get_stock_dividends(self):
        return "Not applicable"

    def get_bonus_issues(self):
        return "Not applicable"

    def get_loans_written_off(self):
        return "Not applicable"

    def get_post_cessation_receipts_amount(self):
        return "Not applicable"

    def get_earlier_year_tax_year_to_be_taxed(self):
        return "Not applicable"

    def get_share_schemes_taxable_amount(self):
        return "Not applicable"

    def get_box_2_is_not_is_use(self):
        return "Not applicable"

    def get_taxable_lump_sums(self):
        return "Not applicable"

    def get_lump_sums_employer_financed_retirement_benefits_scheme(self):
        return "Not applicable"

    def get_redundancy_payments(self):
        return "Not applicable"

    def get_tax_taken_off_boxes_3_to_5(self):
        return "Not applicable"

    def is_box_6_blank_as_tax_inc__in_box_2_of__employment_(self):
        return "Not applicable"

    def get_exemptions_for_amounts_entered_in_box_4(self):
        return "Not applicable"

    def get_compensation_and_lump_sums_up_to__30_000_exemption(self):
        return "Not applicable"

    def get_disability_and_foreign_service_deduction(self):
        return "Not applicable"

    def get_seafarers__earnings_deduction(self):
        return "Not applicable"

    def get_foreign_earnings_not_taxable_in_the_uk(self):
        return "Not applicable"

    def get_foreign_tax_where_tax_credit_not_claimed(self):
        return "Not applicable"

    def get_exempt_overseas_employee_contributions(self):
        return "Not applicable"

    def get_uk_patent_royalty_payments_made(self):
        return "Not applicable"

    def get_subscriptions_for_venture_capital_trust_shares(self):
        return "Not applicable"

    def get_subscriptions_for_enterprise_investment_scheme_shares(self):
        return "Not applicable"

    def get_community_investment_tax_relief(self):
        return "Not applicable"

    def get_annual_payments_made(self):
        return "Not applicable"

    def get_qualifying_loan_interest_payable_in_the_year(self):
        return "Not applicable"

    def get_post_cessation_trade_relief_and_certain_other_losses(self):
        return "Not applicable"

    def get_pre_incorporation_losses(self):
        return "Not applicable"

    def get_maintenance_payments(self):
        return "Not applicable"

    def get_payments_to_a_trade_union_for_death_benefits(self):
        return "Not applicable"

    def get_relief_claimed_on_a_qualifying_distribution(self):
        return "Not applicable"

    def get_shares_under_the_seed_enterprise_investment_scheme(self):
        return "Not applicable"

    def get_box_11_is_not_in_use(self):
        return "Not applicable"

    def get_non_deductible_loan_interest_letting_pship_investments(self):
        return "Not applicable"

    def get_not_applicable(self):
        return "Not applicable"

    def get_earlier_years__losses(self):
        return "Not applicable"

    def get_total_unused_losses_carried_forward(self):
        return "Not applicable"

    def get_relief_now_for_following_year_trade_losses(self):
        return "Not applicable"

    def get_amount_in_box_3_not_subject_to_income_tax_relief_limit(self):
        return "Not applicable"

    def get_tax_year_for_which_you_re_claiming_relief_in_box_3_(self):
        return "Not applicable"

    def get_amount_of_payroll_giving(self):
        return "Not applicable"

    def get_gift_aid_payments_to_non_uk_charities_in_box_6(self):
        return "Not applicable"

    def get_registered_blind_(self):
        return False

    def get_local_authority_or_other_register(self):
        return "Not applicable"

    def get_do_you_want_spouse_s_surplus_allowance(self):
        return "Not applicable"

    def get_should_your_spouse_get_your_surplus_allowance(self):
        return "Not applicable"

    def get_have_you_received_student_loans_company_notification(self):
        return False

    def get_any_employer_deducted_student_loan(self):
        return "Not applicable"

    def get_any_employer_deducted_post_grad_loan(self):
        return "Not applicable"

    def get_how_much_child_benefit__cb__received(self):
        return 0.0

    def get_title(self):
        full_utr = self.get_full_utr()
        person_name = self.person.get_name()
        report_type = self.report_type
        tax_year = self.tax_year

        return f"HMRC {tax_year} {report_type} tax return for {person_name} - UTR {full_utr}\n"

    def get_total_amount_of_allowable_expenses(self):
        return 0

    def get_total_of_any__one_off__payments_in_box_1(self):
        my_payments = self.transactions.fetch_total_by_tax_year_category(
            self.tax_year, "HMRC S pension contribution"
        )
        hmrc_contribution = self.transactions.fetch_total_by_tax_year_category(
            self.tax_year, "HMRC S pension tax relief"
        )
        return my_payments + hmrc_contribution

    def get_total_of_any_other_taxable_state_pensions_and_benefits(self):
        return 0

    def trusts_etc(self):
        return False

    def get_untaxed_foreign_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INT income: interest foreign untaxed"
        )

    def did_you_give_to_charity(self):
        return False

    def are_you_claiming_married_couple_s_allowance(self):
        return False

    def is_trading_income_more_than_vat_registration_cusp(self):
        trading_income = self.get_trading_income()
        vat_registration_cusp = self.get_vat_registration_threshold()

        return trading_income > vat_registration_cusp

    def are_you_affected_by_basis_period_reform(self):
        return False

    def do_you_wish_to_make_an_adjustment_to_your_profits(self):
        return False

    def are_you_a_farmer(self):
        return False

    def were_any_results_already_declared_on_a_previous_return(self):
        return False

    def is_the_basis_period_different_to_the_accounting_period(self):
        return False

    def is_your_business_carried_on_abroad(self):
        return False

    def get_i_need_to_claim__overlap_relief_(self):
        return False

    def get_income__trading_allowance__volunteer_c2_nics(self):
        trading_income = self.get_trading_income()
        trading_allowance = self.get_trading_allowance()
        pay_voluntarily_nics = self.get_do_you_want_to_pay_class_2_nics_voluntarily()

        return trading_income <= trading_allowance and pay_voluntarily_nics

    def get_income__trading_allowance__claim_back_cis(self):
        return False

    def get_loss(self):
        return self.get_trading_expenses() - self.get_trading_income()

    def get_loss_gbp(self):
        return uf.format_as_gbp(self.get_loss())

    def get_profit(self):
        return self.get_trading_income() - self.get_trading_expenses()

    def get_profit_gbp(self):
        return uf.format_as_gbp(self.get_profit())

    def get_income__trading_allowance__made_a_loss(self):
        trading_income = self.get_trading_income()
        trading_allowance = self.get_trading_allowance()
        loss = self.get_loss()
        return trading_income <= trading_allowance and loss > 0

    def do_none_of_these_apply_business_1_page_1(self):
        conditions = [
            self.is_trading_income_more_than_vat_registration_cusp(),
            self.are_you_affected_by_basis_period_reform(),
            self.are_you_a_foster_carer(),
            self.do_you_wish_to_make_an_adjustment_to_your_profits(),
            self.are_you_a_farmer(),
            self.were_any_results_already_declared_on_a_previous_return(),
            self.is_the_basis_period_different_to_the_accounting_period(),
            self.is_your_business_carried_on_abroad(),
            self.get_i_need_to_claim__overlap_relief_(),
            self.get_income__trading_allowance__volunteer_c2_nics(),
            self.get_income__trading_allowance__claim_back_cis(),
            self.get_income__trading_allowance__made_a_loss(),
        ]

        return uf.all_conditions_are_false(conditions)

    def did_none_of_these_apply__class_4_nics_(self):
        conditions = [
            self.were_you_over_state_pension_age_at_tax_year_start(),
            self.were_you_under_16_at_tax_year_start(),
            self.were_you_not_resident_in_uk_during_the_tax_year(),
            self.are_you_a_trustee__executor_or_administrator(),
            self.are_you_a_diver(),
        ]

        return uf.all_conditions_are_false(conditions)

    def get_business_end_date(self):
        return ""

    def get_business_start_date(self):
        return ""

    def is_income___pa___spouse_income___higher_rate_cusp(self):
        total_income_excluding_tax_free_savings = (
            self.get_total_income_excluding_tax_free_savings()
        )
        spouse_total_income = self.get_spouse_total_income()
        personal_allowance = self.get_personal_allowance()
        higher_rate_threshold = self.constants.get_higher_rate_threshold()

        return (
            total_income_excluding_tax_free_savings < personal_allowance
            and spouse_total_income < higher_rate_threshold
        )

    def claim_other_tax_reliefs(self):
        return False

    def have_you_had_any_2023_24_income_tax_refunded(self):
        return False

    def did_you_have_a_tax_advisor(self):
        return False

    def have_you_used_tax_avoidance_schemes(self):
        return False

    def are_you_acting_on_behalf_of_someone_else(self):
        return False

    def get_personal_savings_allowance(self):
        return self.constants.get_personal_savings_allowance()

    def get_starting_rate_limit_for_savings(self):
        return self.constants.get_starting_rate_limit_for_savings()

    def get_savings_basic_rate(self):
        return self.constants.get_savings_basic_rate()

    def get_tax_due_on_untaxed_uk_interest(self):

        # 2023-24 personal allowance is £12,570
        personal_allowance = self.get_personal_allowance()

        # 2023-24 personal savings allowance is £1,000
        personal_savings_allowance = self.get_personal_savings_allowance()

        # 2023-24 limit is £5,000
        starting_rate_limit_for_savings = self.get_starting_rate_limit_for_savings()

        # 2023-24 total allowances is £18,570
        total_allowances = (
            personal_allowance
            + personal_savings_allowance
            + starting_rate_limit_for_savings
        )

        total_income = self.get_total_income()

        untaxed_uk_interest = self.get_untaxed_uk_interest()

        non_interest_income = total_income - untaxed_uk_interest

        interest_free_allowance = max(0, total_allowances - non_interest_income)

        taxable_savings = max(0, untaxed_uk_interest - interest_free_allowance)

        savings_basic_rate = self.get_savings_basic_rate()

        tax_due_on_untaxed_uk_interest = taxable_savings * savings_basic_rate

        return tax_due_on_untaxed_uk_interest

    def get_untaxed_uk_interest(self):
        person_code = self.person_code
        tax_year = self.tax_year

        return self.get_year_category_total(
            tax_year, f"HMRC {person_code} INT income: interest UK untaxed"
        )

    def have_you_uk_rental_property(self):
        # search the transactions table for any records in this tax year
        # which have a UKP income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(DISTINCT Category)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} UKP income%"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def get_vat_registration_threshold(self):
        return self.constants.get_vat_registration_threshold()

    def get_year_category_total(self, tax_year, category):
        return self.transactions.fetch_total_by_tax_year_category(tax_year, category)

    def get_your_date_of_birth(self):
        return self.person.get_uk_date_of_birth()

    def get_your_name_and_address(self):
        return "Leave blank unless changed from previous year"

    def get_your_national_insurance_number(self):
        return self.person.get_national_insurance_number()

    def get_your_phone_number(self):
        return self.person.get_phone_number()

    def is_the_underpaid_tax_amount_for_earlier_years_correct(self) -> bool:
        return True

    def is_the_underpaid_tax_amount_for_this_tax_year_correct(self) -> bool:
        return True

    def is_the_address_shown_above_correct(self):
        return True

    def is_student_loan_repayment_due(self) -> bool:
        return False

    def is_postgraduate_loan_repayment_due(self) -> bool:
        return False

    def list_categories(self):
        query = (
            self.transactions.query_builder()
            .select_raw("DISTINCT Category")
            .where(
                f'"Tax year" = "{self.tax_year}" AND "Category" LIKE "HMRC {self.person_code}%" ORDER BY Category'
            )
            .build()
        )

        categories = self.sql.fetch_all(query)
        for row in categories:
            print(row[0])

    def position_answer(self, string_list) -> str:
        if self.report_type == HMRC.ONLINE_REPORT:
            widths = [55]  # Define column widths
        else:
            widths = [5, 60]

        how_many = len(widths)  # How many columns to format

        # Use zip to pair strings with widths and format them in one step
        formatted_parts = [
            f"{string:<{width}}"
            for string, width in zip(string_list[:how_many], widths)
        ]

        # Join the formatted parts and append the fourth string without formatting
        return "".join(formatted_parts) + string_list[how_many]

    def print_end_of_tax_return(self):
        person_name = self.person.get_name()
        report_type = self.report_type
        tax_year = self.tax_year
        print(f"\nEnd of {tax_year} {report_type} tax return for {person_name}\n")
        print(
            "============================================================================\n"
        )

    def print_formatted_answer(
        self, question, section, header, box, answer, information
    ):
        self.l.debug("print_formatted_answer")
        self.l.debug(f"\n{question}\n")
        self.l.debug(f"{section} - {header} - Box {box}")
        self.l.debug(f"answer: {answer}")
        self.l.debug(f"information: {information}")

        if section != self.previous_section:
            self.previous_section = section
            print(f"\n\n{section.upper()}\n")

        if header != self.previous_header:
            self.previous_header = header
            print(f"\n{header.upper()}\n")

        if isinstance(answer, bool):
            answer = "Yes" if answer else "No"
        elif isinstance(answer, float):
            answer = f"£{answer:,.2f}"
        elif isinstance(answer, int):
            answer = f"{answer:,}"
        elif isinstance(answer, str):
            pass  # No change needed for strings
        else:
            answer = str(answer)

        box = uf.crop(box, " (GBP)")

        if self.report_type == HMRC.ONLINE_REPORT:
            formatted_answer = self.position_answer([box, answer])
        else:
            formatted_answer = self.position_answer([box, question, answer])

        if len(information):
            print(information)

        print(formatted_answer)

    def print_report(self, report_type):
        self.report_type = report_type

        answers = self.get_answers()

        self.print_title()

        for question, section, header, box, answer, information in answers:
            self.print_formatted_answer(
                question, section, header, box, answer, information
            )

        self.print_end_of_tax_return()

    def print_reports(self):
        for report in HMRC.REPORTS:
            self.print_report(report)

    def print_title(self):
        print(self.get_title())

        self.previous_section = ""
        self.previous_header = ""

    def were_there_income_tax_losses(self):
        return False

    def were_you_employed_in_this_tax_year(self) -> bool:
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(*)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} EMP%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0

    def were_you_self_employed_in_this_tax_year(self) -> bool:
        # search the transactions table for any records in this tax year
        # which have an employment income category for the current person
        person_code = self.person.code
        tax_year = self.tax_year
        query = (
            self.transactions.query_builder()
            .select_raw("COUNT(*)")
            .where(
                f'"Tax year"="{tax_year}" AND "Category" LIKE "HMRC {person_code} SES%income"'
            )
            .build()
        )

        how_many = self.sql.fetch_one_value(query)

        return how_many > 0
